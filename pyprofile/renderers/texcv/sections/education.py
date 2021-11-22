import inspect

from pyprofile.renderers.texcv import templates

GRADE_TEX_MAP = {'A*': 'A${{^*}}$', 'A': 'A'}


def generate(profile):
    cventries = []

    universities = profile["education"].get('university', [])
    for university in universities:
        cventry = templates.cventry(
            university.get('institution'),
            f"{university.get('degree')} {university.get('course')} - {university.get('classification')}",
            university.get('college'),
            university.get('start_date'),
            university.get('end_date'),
            university.get('achievements')
        )
        cventries.append(cventry)

    schools = profile["education"].get('school', [])
    for school in schools:
        a_levels_cvitem = _a_levels_to_cvitem(school)
        gcses_cvitem = _gcses_to_cvitem(school)
        cventry = templates.cventry(
            school.get('name'),
            None,
            school.get('location'),
            school.get('start_date'),
            school.get('end_date'),
            [a_levels_cvitem, gcses_cvitem],
            vspace="-0.5cm"
        )
        cventries.append(cventry)

    cvsection = templates.cvsection('Education', cventries)

    return inspect.cleandoc(cvsection)


def _gcses_to_cvitem(school):
    gcses = "~~·~~".join(
        [f"\\textbf{{{gcse['count']}{GRADE_TEX_MAP[gcse['grade']]}}}s" for gcse in school.get('gcses')]
    )
    gcses_cvitem = f"\\textit{{GCSEs:}} {gcses}"
    return gcses_cvitem


def _a_levels_to_cvitem(school):
    a_levels = "~~·~~".join(
        [f"\\textbf{{{GRADE_TEX_MAP[a_level['grade']]}}} {a_level['name']}" for a_level in school.get('a_levels')]
    )
    a_levels_cvitem = f"\\textit{{A-Levels:}} {a_levels}"
    return a_levels_cvitem
