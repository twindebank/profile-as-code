import os

import pyprofile.transformers.texcv as texcv
from pyprofile import loading
from pyprofile.utils import recursively_replace_dict_str

TEX_SPECIAL_CHARS = '\\&%$#_{}~^'


def main(profile_file, resume_save_dir):
    _set_up_tex_dir(resume_save_dir)

    profile = loading.load_profile(profile_file)

    profile = _escape_chars(profile, TEX_SPECIAL_CHARS)

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
