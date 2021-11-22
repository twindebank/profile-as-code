import pprint
import sys
from copy import deepcopy
from dataclasses import dataclass
from typing import Dict

import cerberus
from deepmerge import always_merger
from path import Path

from pyprofile.io import load_yaml, load_and_concat_raw_yaml
from pyprofile.renderers.texcv.utils import recursively_censor_dict_strs


@dataclass
class Profile:
    public_fields: Dict
    private_fields: Dict
    specs = Path(__file__).parent / "contracts/profile.yml"
    validator = cerberus.Validator(load_yaml(specs))

    @classmethod
    def from_ymls(cls, path):
        public_fields = load_and_concat_raw_yaml(path, '*.yml')
        private_fields = load_and_concat_raw_yaml(path / 'private', '*.yml')
        return cls(public_fields, private_fields)

    def __post_init__(self):
        self.uncensored = always_merger.merge(self.public_fields, self.private_fields)
        censored_private_fields = recursively_censor_dict_strs(deepcopy(self.private_fields), "<CENSORED>")
        self.censored = always_merger.merge(deepcopy(self.public_fields), censored_private_fields)

        if not self.validator.validate(self.uncensored):
            pprint.pprint(self.validator.errors)
            sys.exit(1)

        if not self.validator.validate(self.censored):
            pprint.pprint(self.validator.errors)
            sys.exit(1)
