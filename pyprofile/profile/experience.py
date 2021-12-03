import datetime
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any

from ruamel.yaml import YAML

yaml = YAML()


@dataclass
class Description:
    short: str
    long: Optional[str] = None

    def __post_init__(self):
        if not self.long:
            self.long = self.short


@dataclass
class Experience:
    key: str
    name: str
    location: str
    job_title: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    description: Description

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        d = deepcopy(d)
        d['description'] = Description(**d['description'])
        return cls(**d)


class Experiences:
    file = "experience.yml"

    @classmethod
    def from_yaml(cls, path: Path):
        contents = yaml.load(path / cls.file)
        return [Experience.from_dict(e) for e in contents]
