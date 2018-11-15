import os

import click

import pyprofile.transformers.texcv as texcv


@click.command()
@click.argument('profile_file')
@click.argument('resume_dir')
def generate_tex(profile_file, resume_dir):
    set_up_tex_dir(resume_dir)

    profile = texcv.load_profile.load_and_escape(profile_file, special_chars='&%$#_{}~^\\')

    pages_dir = os.path.join(resume_dir, 'resume')
    structure = {
        'resume': resume_dir,
        'education': pages_dir,
        'experience': pages_dir,
        'skills': pages_dir
    }

    for page, directory in structure.items():
        tex = getattr(texcv.pages, page).generate(profile)
        write_tex(page, directory, tex)


def set_up_tex_dir(tex_dir):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)
    os.system(f"cp -r pyprofile/transformers/texcv/_tex_resources/* {tex_dir}/")


def write_tex(filename, tex_dir, content):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)

    path = os.path.join(tex_dir, f"{filename}.tex")
    with open(path, 'w') as texfile:
        texfile.write(content)


if __name__ == '__main__':
    generate_tex()
