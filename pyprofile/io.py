import glob
import logging
import pprint

import cerberus
from ruamel import yaml as yaml

PROFILE_SPECS = 'contracts/profile.yml'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_profiles(profile_directory):
    profile_public = load_profile(profile_directory)
    profile_private = load_profile(profile_directory, censored=False)
    return profile_public, profile_private


def load_profile(profile_directory):

    profile_yaml = '\n'.join([private_yaml, public_yaml])


    return profile


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def load_and_concat_raw_yaml(directory, file_pattern):
    filenames = sorted(glob.glob(f"{directory}/{file_pattern}"))
    separate = []
    for filename in filenames:
        with open(filename) as f:
            separate.append(f.read())
    concatenated = '\n'.join(separate)
    return concatenated
