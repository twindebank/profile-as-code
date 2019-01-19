import glob
import logging
import pprint

import click
import cerberus

from ruamel import yaml as yaml

CONFIG_SPECS = 'specs/config.yml'
PROFILE_SPECS = 'specs/profile.yml'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_profiles(profile_directory):
    profile_public = load_profile(profile_directory)
    profile_private = load_profile(profile_directory, censored=False)
    return profile_public, profile_private


def load_profile(profile_directory, censored=True):
    public_yaml = _load_and_concat_raw_yaml(profile_directory, '*.yml')
    private_yaml = _load_and_concat_raw_yaml(profile_directory, '.*.yml')
    if censored:
        private_yaml = _censor_private_raw_yaml(private_yaml)
    profile_yaml = '\n'.join([private_yaml, public_yaml])
    profile = yaml.round_trip_load(
        profile_yaml,
        preserve_quotes=True
    )
    del profile['private']

    # profile = dict(profile)

    validator = cerberus.Validator(load_yaml(PROFILE_SPECS))
    if not validator.validate(profile):
        pprint.pprint(validator.errors)
        raise ValueError('Profile YAML not valid')

    return profile


def load_yaml(path):
    yaml_fd = open(path)
    yaml_loaded = yaml.safe_load(
        yaml_fd
    )
    yaml_fd.close()
    return yaml_loaded


def _load_and_concat_raw_yaml(directory, file_pattern):
    filenames = sorted(glob.glob(f"{directory}/{file_pattern}"))
    concatenated = '\n'.join([open(f).read() for f in filenames])
    return concatenated


def _censor_private_raw_yaml(private_yaml):
    """Have to censor manually as loading in yaml fucks with aliases/anchors"""
    lines = private_yaml.split('\n')
    censored_lines = []
    for line in lines[1:]:
        if line:
            key, anchor_and_val = line.split('&')
            anchor, *_ = anchor_and_val.split(' ')
            censored_line = f"{key}&{anchor} <CENSORED>"
            censored_lines.append(censored_line)
    censored_lines.insert(0, lines[0])
    censored_yaml = '\n'.join(censored_lines)

    return censored_yaml


class YamlConfigLoader(click.Option):
    """Loads YAML from a Click option argument, if no input then loads defaults from spec."""

    def type_cast_value(self, ctx, value):
        validator = cerberus.Validator(load_yaml(CONFIG_SPECS))
        try:
            config = load_yaml(value)
        except Exception as e:
            logger.exception(e)
            raise click.BadParameter(value)

        if not validator.validate(config):
            logger.error(str(validator.errors))
            raise click.BadParameter(value)

        return config
