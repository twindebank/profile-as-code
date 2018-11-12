import os

import pyprofile.parsing
import pyprofile.texcv as texcv


def generate_tex(path='profile-public.yml', save_dir='tex-cv'):
    set_up_tex_dir(save_dir)

    profile = pyprofile.parsing.load(path, special_chars='&%$#_{}~^\\')

    res = texcv.pages.resume.generate(profile)
    write_tex('resume', save_dir, res)

    pages_dir = os.path.join(save_dir, 'resume')

    edu = texcv.pages.education.generate(profile)
    write_tex('education', pages_dir, edu)

    exp = texcv.pages.experience.generate(profile)
    write_tex('experience', pages_dir, exp)

    skills = texcv.pages.skills.generate(profile)
    write_tex('skills', pages_dir, skills)



def set_up_tex_dir(tex_dir):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)

    os.system(f"cp -r pyprofile/texcv/resources/* {tex_dir}/")


def write_tex(filename, tex_dir, content):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)

    path = os.path.join(tex_dir, f"{filename}.tex")
    with open(path, 'w') as texfile:
        texfile.write(content)


generate_tex()
