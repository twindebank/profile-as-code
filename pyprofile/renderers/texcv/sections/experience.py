import inspect

from pyprofile.renderers.texcv import templates


def generate(profile):
    experiences = profile["experience"]

    cventries = []
    for experience in experiences:
        cventry = templates.cventry(
            experience.get('name', {}).get('short'),
            experience.get('job_title'),
            experience.get('location'),
            experience.get('start_date'),
            experience.get('end_date'),
            experience.get('description', {}).get('short', [])
        )

        cventries.append(cventry)

    cvsection = templates.cvsection('Experience', cventries)

    return inspect.cleandoc(cvsection)
