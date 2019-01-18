import logging

import click

from pyprofile.transformers import validyaml, texcv, website
import pyprofile.loading as loading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def config_option():
    """Click Option decorator to load config from a YAML file."""
    return click.option(
        '-c', '--config',
        default='default_config.yml',
        type=str,
        cls=loading.YamlConfigOption,
        help="Path of YAML config file."
    )


@click.group()
def cli():
    pass


@cli.command()
@config_option()
def validate_and_concat(config):
    """Validate profile YAML files and concatenate them into a single file."""
    profile_public, profile_private = loading.load_profiles(profile_directory=config['inputs']['profile_directory'])
    validyaml.generate.main(profile_public, config['outputs']['profile_yaml']['censored'])
    validyaml.generate.main(profile_private, config['outputs']['profile_yaml']['uncensored'])


@cli.command()
@config_option()
def generate_tex_cv(config):
    """Generate PDF cv using XeLaTeX."""
    profile_public, profile_private = loading.load_profiles(profile_directory=config['inputs']['profile_directory'])
    texcv.generate.main(profile_public, config['outputs']['cv']['censored'],
                        exclude_experience=config['outputs']['cv']['exclude'])
    texcv.generate.main(profile_private, config['outputs']['cv']['uncensored'],
                        exclude_experience=config['outputs']['cv']['exclude'])


@cli.command()
@config_option()
def generate_website(config):
    """Generate website with CV and links."""
    profile_public = loading.load_profile(profile_directory=config['inputs']['profile_directory'], censored=True)
    website.generate.main(profile_public, config['outputs']['website'])


@cli.command()
@config_option()
def generate_all(config):
    profile_public, profile_private = loading.load_profiles(profile_directory="profile")

    validyaml.generate.main(profile_public, config['outputs']['profile_yaml']['censored'])
    validyaml.generate.main(profile_private, config['outputs']['profile_yaml']['uncensored'])

    texcv.generate.main(profile_public, config['outputs']['cv']['censored'],
                        exclude_experience=config['outputs']['cv']['exclude'])
    texcv.generate.main(profile_private, config['outputs']['cv']['uncensored'],
                        exclude_experience=config['outputs']['cv']['exclude'])

    website.generate.main(profile_public, config['outputs']['website'])


if __name__ == '__main__':
    cli()
