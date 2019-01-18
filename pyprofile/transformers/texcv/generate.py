import logging
import os
import docker

import pyprofile.transformers.texcv as texcv
from pyprofile.utils import recursively_replace_dict_str

TEX_SPECIAL_CHARS = '\\&%$#_{}~^'
MODULE_DIR = os.path.dirname(__file__)
LATEX_SOURCE = os.path.join(MODULE_DIR, '_source')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(profile, cv_filename, cv_save_dir='.', exclude_experience=()):
    os.system(f"cp -r {LATEX_SOURCE} ._latex_source_bak/")

    cv_path = os.path.join(cv_save_dir, cv_filename)

    logger.info(f"Generating tex cv at '{cv_path}.pdf'")

    profile = _escape_chars(profile, TEX_SPECIAL_CHARS)

    profile['experience'] = [exp for exp in profile['experience'] if exp['key'] not in exclude_experience]

    pages_dir = os.path.join(LATEX_SOURCE, 'resume')
    structure = {
        'resume': LATEX_SOURCE,
        'education': pages_dir,
        'experience': pages_dir,
        'skills': pages_dir
    }

    for page, directory in structure.items():
        tex = getattr(texcv.pages, page).generate(profile)
        _write_tex(page, directory, tex)

    client = docker.from_env()

    volumes = {
        os.path.join(os.getcwd(), LATEX_SOURCE): {'bind': '/source', 'mode': 'rw'}
    }

    output = client.containers.run(
        image='schickling/latex',
        command='xelatex resume.tex',
        remove=True,
        volumes=volumes,
        stdout=True,
        stderr=True
    )
    os.system(f"cp -r {os.path.join(LATEX_SOURCE, 'resume.pdf')} {cv_path}")

    logger.info(output.decode("utf-8"))

    logger.info(f"Output saved to '{cv_path}'")

    os.system(f"rm -rf {LATEX_SOURCE}")
    os.system(f"cp -r ._latex_source_bak/ {LATEX_SOURCE}")
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
