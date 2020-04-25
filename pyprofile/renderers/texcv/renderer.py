import os
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List

import docker
from loguru import logger
from path import Path

from pyprofile.renderers.base import Renderer
from pyprofile.renderers.texcv import sections
from pyprofile.renderers.texcv.utils import recursively_replace_dict_str


@dataclass
class CVRenderer(Renderer):
    name: str
    censor: bool = True
    exclude_experience: List[str] = field(default_factory=list)
    exclude_education: List[str] = field(default_factory=list)

    special_tex_chars = '\\&%$#_{}~^'
    latex_source = Path(__file__).parent / '_source'
    latex_img = 'schickling/latex:latest'

    def render(self, profile, output_dir):
        cv = deepcopy(profile.censored if self.censor else profile.uncensored)

        os.system(f"cp -r {self.latex_source} ._latex_source_bak/")

        cv_path = output_dir / self.name

        logger.info(f"Generating tex cv at '{cv_path}'")

        profile = _escape_chars(cv, self.special_tex_chars)

        profile['experience'] = [exp for exp_name, exp in profile['experience'].items() if
                                 exp_name not in self.exclude_experience]
        profile['education'] = {edu_name: edu for edu_name, edu in profile['education'].items() if
                                edu_name not in self.exclude_education}
        pages_dir = os.path.join(self.latex_source, 'resume')
        structure = {
            'resume': self.latex_source,
            'education': pages_dir,
            'experience': pages_dir,
            'skills': pages_dir
        }

        for section, directory in structure.items():
            tex = getattr(sections, section).generate(cv)
            _write_tex(section, directory, tex)

        client = docker.from_env()

        volumes = {
            os.path.join(os.getcwd(), self.latex_source): {'bind': '/source', 'mode': 'rw'}
        }

        logger.info(f"Pulling image '{self.latex_img}'...")
        client.images.pull(self.latex_img)
        output = client.containers.run(
            image=self.latex_img,
            command='xelatex resume.tex',
            remove=True,
            volumes=volumes,
            stdout=True,
            stderr=True
        )
        os.system(f"cp -r {os.path.join(self.latex_source, 'resume.pdf')} {cv_path}")

        logger.info(output.decode("utf-8"))

        logger.info(f"Output saved to '{cv_path}'")

        os.system(f"rm -rf {self.latex_source}")
        os.system(f"cp -r ._latex_source_bak/ {self.latex_source}")
        os.system(f"rm -r ._latex_source_bak")


def _write_tex(filename, tex_dir, content):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)

    path = os.path.join(tex_dir, f"{filename}.tex")
    with open(path, 'w') as texfile:
        texfile.write(content)


def _escape_chars(dct, chars):
    for char in chars:
        dct = recursively_replace_dict_str(dct, char, f"\\{char}")
    return dct


if __name__ == '__main__':
    a = __file__
    print(a)
