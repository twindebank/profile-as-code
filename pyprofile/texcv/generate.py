import pyprofile.profile
from pyprofile.texcv.pages import resume


def generate_tex(path='profile-private.yml'):
    profile = pyprofile.profile.load(path)

    res = resume.generate(profile)

    pass

generate_tex()