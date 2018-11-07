import inspect


def generate(profile):
    experiences = profile["experience"]

    cventries = []
    for experience in experiences:

        cvitems = "\n".join([f"\item{{{cvitem}}}" for cvitem in experience.get('description', {}).get('short', [])])

        cventry = f"""
        \cventry
        {{{experience.get('job_title', '')}}}
        {{{experience.get('name', {}).get('short', '')}}}
        {{{experience.get('location')}}}
        {{{f"{experience.get('date_from', '')} – {experience.get('date_to', '')}"}}}

        {{
            \\begin{{cvitems}}
            
            {cvitems}
            
            \end{{cvitems}}
        }}
        """
        cventries.append(cventry)

    cventries = "\n".join(cventries)

    page = f"""
           \cvsection{{Experience}}
           \\begin{{cventries}}
           {cventries}
           \end{{cventries}}
    """

    return inspect.cleandoc(page)
