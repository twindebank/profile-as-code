from typing import Protocol

from pyprofile.profile import Profile


class Transformer(Protocol):
    name: str
    description: str

    def transform(self, profile: Profile):
        ...
