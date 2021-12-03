from dataclasses import dataclass
from pathlib import Path
from typing import Collection

from ruamel.yaml import YAML

from pyprofile.profile.education import Education
from pyprofile.profile.experience import Experience, Experiences
from pyprofile.profile.general import General
from pyprofile.profile.personal_project import PersonalProject, PersonalProjects
from pyprofile.profile.professional_project import ProfessionalProject, ProfessionalProjects
from pyprofile.profile.talk import Talk, Talks

yaml = YAML()


@dataclass
class Profile:
    general: General
    experience: Collection[Experience]
    education: Education
    personal_projects: Collection[PersonalProject]
    professional_projects: Collection[ProfessionalProject]
    talks: Collection[Talk]

    @classmethod
    def from_yamls(cls, path: Path):
        return cls(
            general=General.from_yaml(path),
            education=Education.from_yaml(path),
            experience=Experiences.from_yaml(path),
            personal_projects=PersonalProjects.from_yaml(path),
            professional_projects=ProfessionalProjects.from_yaml(path),
            talks=Talks.from_yaml(path),
        )
