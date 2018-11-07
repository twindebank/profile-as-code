import os

import pyprofile.profile
import pyprofile.texcv as texcv


def set_up_tex_dir(tex_dir):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)

    os.system(f"cp -r pyprofile/texcv/resources/* {tex_dir}/")


def generate_tex(path='profile-public.yml', save_dir='tex-cv'):
    set_up_tex_dir(save_dir)

    profile = pyprofile.profile.load(path)

    res = texcv.pages.resume.generate(profile)

    write_tex('resume', save_dir, res)


def write_tex(filename, save_dir, content):
    path = os.path.join(save_dir, f"{filename}.tex")
    with open(path, 'w') as texfile:
        texfile.write(content)


generate_tex()
