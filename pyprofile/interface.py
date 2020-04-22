import logging

import pyprofile.io as loading
from pyprofile.transformers import validyaml, texcv, website

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_and_concat(config):
    """Validate profile YAML files and concatenate them into a single file."""
    profile_public, profile_private = loading.load_profiles(profile_directory=config['inputs']['profile_directory'])
    validyaml.generate.main(profile_public, config['outputs']['profile_yaml']['censored'])
    validyaml.generate.main(profile_private, config['outputs']['profile_yaml']['uncensored'])


def generate_tex_cv(config):
    """Generate PDF cv using XeLaTeX."""
    profile_public, profile_private = loading.load_profiles(profile_directory=config['inputs']['profile_directory'])
    texcv.generate.main(profile_public, config['outputs']['cv']['censored'],
                        exclude_experience=config['outputs']['cv']['exclude'])
    texcv.generate.main(profile_private, config['outputs']['cv']['uncensored'],
                        exclude_experience=config['outputs']['cv']['exclude'])


def generate_website(config):
    """Generate website with CV and links."""
    profile_public = loading.load_profile(profile_directory=config['inputs']['profile_directory'], censored=True)
    website.generate.main(profile_public, config['outputs']['website']['directory'])


def generate_all(config):
    profile_public, profile_private = loading.load_profiles(profile_directory="profile")

    validyaml.generate.main(profile_public, config['outputs']['profile_yaml']['censored'])
    validyaml.generate.main(profile_private, config['outputs']['profile_yaml']['uncensored'])

    texcv.generate.main(profile_public, config['outputs']['cv']['censored'],
                        exclude_experience=config['outputs']['cv']['exclude'])
    texcv.generate.main(profile_private, config['outputs']['cv']['uncensored'],
                        exclude_experience=config['outputs']['cv']['exclude'])

    website.generate.main(profile_public, config['outputs']['website']['directory'])
