import inspect

from pyprofile.texcv import templates


def generate(profile):
    skills = [skill['name'] for skill in profile.get('skills')]
    cvitem = " ~~·~~ ".join(skills)
    cventry = templates.cventry(cvitems=[cvitem])
    cvsection = templates.cvsection('Skills', [cventry])
    return inspect.cleandoc(cvsection)
