import logging
import os
import docker

import pyprofile.transformers.texcv as texcv
from pyprofile import loading
from pyprofile.utils import recursively_replace_dict_str

TEX_SPECIAL_CHARS = '\\&%$#_{}~^'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(profile_file, resume_save_dir, exclude_experience=()):
    logger.info(f"Loading profile from '{profile_file}' and generating tex cv in '{resume_save_dir}'")

    _set_up_tex_dir(resume_save_dir)

    profile = loading.load_profile(profile_file)

    profile = _escape_chars(profile, TEX_SPECIAL_CHARS)

    profile['experience'] = [exp for exp in profile['experience'] if exp['key'] not in exclude_experience]

    pages_dir = os.path.join(resume_save_dir, 'resume')
    structure = {
        'resume': resume_save_dir,
        'education': pages_dir,
        'experience': pages_dir,
        'skills': pages_dir
    }

    for page, directory in structure.items():
        tex = getattr(texcv.pages, page).generate(profile)
        _write_tex(page, directory, tex)

    logger.info(f"Output saved to '{resume_save_dir}'")

    client = docker.from_env()

    volumes = {
        os.path.join(os.getcwd(), resume_save_dir): {'bind': '/source', 'mode': 'rw'}
    }

    output = client.containers.run(
        image='schickling/latex',
        # command='ls -lash /source',
        command='xelatex resume.tex',
        remove=True,
        volumes=volumes,
        stdout=True,
        stderr=True
    )

    logger.info(output.decode("utf-8"))


def _set_up_tex_dir(tex_dir):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)
    os.system(f"cp -r pyprofile/transformers/texcv/_tex_resources/* {tex_dir}/")


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
