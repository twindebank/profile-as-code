import inspect

from pyprofile.renderers.texcv import templates


def generate(profile):
    skills = profile.get('skills', [])
    cvitem = " ~~·~~ ".join(skills)
    cventry = templates.cventry(cvitem="\\newline " + cvitem, vspace="-3em")
    cvsection = templates.cvsection('Skills', [cventry])
    return inspect.cleandoc(cvsection)
