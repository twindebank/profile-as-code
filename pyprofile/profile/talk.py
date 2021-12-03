from dataclasses import dataclass
from pathlib import Path

from ruamel.yaml import YAML

from pyprofile.profile.experience import Description

yaml = YAML()


@dataclass
class Talk:
    event: str
    title: str
    url: str
    video: str
    description: Description


class Talks:
    file = "talks.yml"

    @classmethod
    def from_yaml(cls, path: Path):
        contents = yaml.load(path / cls.file)
        talks = []
        for talk in contents:
            talk['description'] = Description(**talk['description'])
            talks.append(talk)
        return talks
