import inspect

from pyprofile.renderers.texcv import templates


def generate(profile):
    skills = profile.get('skills', [])
    cvitem = " ~~·~~ ".join(skills)
    cventry = templates.cventry(cvitems=[cvitem], vspace="-1em")
    cvsection = templates.cvsection('Skills', [cventry])
    return inspect.cleandoc(cvsection)
