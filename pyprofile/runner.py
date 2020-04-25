from dataclasses import dataclass
from typing import List

from path import Path

from pyprofile.profile import Profile
from pyprofile.renderers.base import Renderer


@dataclass
class Runner:
    renderers: List[Renderer]
    input_dir: Path
    output_dir: Path

    def __post_init__(self):
        self.profile = Profile.from_ymls(self.input_dir)

    def render(self):
        for renderer in self.renderers:
            renderer.render(self.profile, self.output_dir)
