import inspect


def cvsection(section, cventries):
    cventries = "\n".join(cventries)

    tex = f"""
    \cvsection{{{section}}}
    \\begin{{cventries}}
        {cventries}
    \end{{cventries}}
    """
    return inspect.cleandoc(tex)


def cventry(h1_left=None, h2_left=None, h1_right=None, start_date=None, end_date=None, cvitems=None, vspace=None, cvitem=None):
    date_str = _gen_date_str(start_date, end_date)
    vspace = f"\\vspace{{{vspace}}}" if vspace else ''

    cv_items_block = f"""
        \\begin{{cvitems}}
            {_cvitems(cvitems)}
        \end{{cvitems}}
    """ if cvitems else cvitem

    tex = f"""
        \cventry
            {{{_to_str(h2_left)}}}
            {{{_to_str(h1_left)}}}
            {{{_to_str(h1_right)}}}
            {{{date_str}}}
            {{{vspace}
                {inspect.cleandoc(cv_items_block)}
            }}
            \\vspace{{-0.2cm}}
    """
    return tex


def _gen_date_str(start_date, end_date):
    if start_date and end_date:
        date_str = f"{start_date} - {end_date}"
    elif start_date:
        date_str = start_date
    elif end_date:
        date_str = end_date
    else:
        date_str = ''
    return date_str


def _cvitems(items):
    tex = "\n                    ".join(
        [_cvitem(item) for item in items]
    )
    return tex


def _cvitem(item):
    tex = f"\item{{{item.strip()}}}"
    return inspect.cleandoc(tex)


def _to_str(string):
    return string if string is not None else ''
