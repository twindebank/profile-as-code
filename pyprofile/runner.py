import pprint
from copy import deepcopy
from dataclasses import dataclass
from typing import Type, List, Dict

import cerberus
from deepmerge import always_merger
from path import Path

from pyprofile.io import load_and_concat_raw_yaml, load_yaml, PROFILE_SPECS
from pyprofile.renderers.base import Renderer
from pyprofile.renderers.texcv.utils import recursively_censor_dict_strs


@dataclass
class Profile:
    private_fields: Dict
    public_fields: Dict
    validator = cerberus.Validator(load_yaml(PROFILE_SPECS))

    @classmethod
    def from_ymls(cls, path):
        public_fields = load_and_concat_raw_yaml(path, '*.yml')
        private_fields = load_and_concat_raw_yaml(path, '.*.yml')
        return cls(public_fields, private_fields)

    def __post_init__(self):
        self.uncensored = always_merger.merge(self.public_fields, self.private_fields)
        censored_private_fields = recursively_censor_dict_strs(deepcopy(self.private_fields), "<CENSORED>")
        self.censored = always_merger.merge(self.private_fields, censored_private_fields)

        if not self.validator.validate(self.uncensored):
            pprint.pprint(self.validator.errors)
            raise ValueError('Profile YAML not valid')


@dataclass
class Runner:
    renderers: List[Type[Renderer]]
    input_dir: Path
    output_dir: Path

    def __post_init__(self):
        self.profile = Profile.from_ymls(self.input_dir)

    def render(self):
        for renderer in self.renderers:
            pass
