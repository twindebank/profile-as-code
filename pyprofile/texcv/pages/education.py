import inspect


def generate(profile):
    universities = profile["education"].get('university')
    schools = profile["education"].get('school')

    university_tex = []
    for university in universities:
        cvitems = "\n                    ".join(
            [f"\item{{{cvitem.strip()}}}" for cvitem in university.get('achievements')]
        )

        tex = f"""
        \cventry
            {{{university.get('degree')} {university.get('course')} - Classification: {university.get(
            'classification')}}}
            {{{university.get('institution')}}}
            {{{university.get('college')}}}
            {{{university.get('start_date')} - {university.get('end_date')}}}
            {{
              \\begin{{cvitems}}
                    {cvitems}
                \end{{cvitems}}
            }}
        """

        university_tex.append(tex)

    school_tex = []
    for school in schools:
        grade_tex_map = {'A*': 'A${{^*}}$', 'A': 'A'}
        a_levels = "~~·~~".join(
            [f"\\textbf{{{grade_tex_map[a_level['grade']]}}} {a_level['name']}" for a_level in school.get('a_levels')]
        )
        gcses = "~~·~~".join(
            [f"\\textbf{{{gcse['count']}{grade_tex_map[gcse['grade']]}}}s" for gcse in school.get('gcses')]
        )
        tex = f"""
        \cventry
            {{}}
            {{{school.get('name')}}}
            {{{school.get('location')}}}
            {{{school.get('start_date')} - {school.get('end_date')}}}
            {{\vspace{{-0.5cm}}
              \\begin{{cvitems}}
                \item {{\\textit{{A-Levels:}} {a_levels}
                \item {{\\textit{{GCSEs:}} {gcses}
              \end{{cvitems}}
            }}
        """
        school_tex.append(tex)

    university_cventries = "\n".join(university_tex)
    school_cventries = "\n".join(school_tex)
    page = f"""
    \cvsection{{Education}}
    \\begin{{cventries}}
        
        {university_cventries}
        {school_cventries}
    
    \end{{cventries}}
    """

    return inspect.cleandoc(page)
