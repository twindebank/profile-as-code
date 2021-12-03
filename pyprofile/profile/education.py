import datetime
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Collection

from ruamel.yaml import YAML

yaml = YAML()


@dataclass
class University:
    institution: str
    college: str
    location: str
    degree: str
    course: str
    classification: str
    start_date: datetime.date
    end_date: datetime.date
    achievements: Collection[str]


@dataclass
class ALevel:
    name: str
    grade: str


@dataclass
class GCSE:
    grade: str
    count: int


@dataclass
class School:
    name: str
    location: str
    start_date: str
    end_date: str
    a_levels: Collection[ALevel]
    gcses: Collection[GCSE]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        d = deepcopy(d)
        d['a_levels'] = [ALevel(**a) for a in d['a_levels']]
        d['gcses'] = [GCSE(**a) for a in d['gcses']]
        return cls(**d)


@dataclass
class Education:
    university: Collection[University]
    school: Collection[School]

    file = "education.yml"

    @classmethod
    def from_yaml(cls, path: Path):
        contents = yaml.load(path / cls.file)
        return cls(
            university=[University(**u) for u in contents['university']],
            school=[School.from_dict(s) for s in contents['school']]
        )
