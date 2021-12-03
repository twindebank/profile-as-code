from dataclasses import dataclass
from pathlib import Path

from ruamel.yaml import YAML

yaml = YAML()


@dataclass
class PersonalProject:
    name: str
    url: str
    description: str


class PersonalProjects:
    file = "personal-projects.yml"

    @classmethod
    def from_yaml(cls, path: Path):
        contents = yaml.load(path / cls.file)
        return [PersonalProject(**p) for p in contents]
