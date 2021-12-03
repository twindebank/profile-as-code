import datetime
from dataclasses import dataclass
from pathlib import Path

from ruamel.yaml import YAML

yaml = YAML()


@dataclass
class General:
    first_name: str
    last_name: str
    mobile: str
    email: str
    homepage: str
    git: str
    linkedin: str
    address: str
    github: str
    bio: str
    dob: datetime.datetime

    file = "general.yml"

    @classmethod
    def from_yaml(cls, path: Path):
        contents = yaml.load(path / cls.file)
        return cls(**contents)
