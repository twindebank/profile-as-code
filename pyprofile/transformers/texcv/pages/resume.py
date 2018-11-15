import inspect


def generate(profile):
    basic = profile['basic_details']
    preamble = """
        %!TEX TS-program = xelatex
        %!TEX encoding = UTF-8 Unicode
        % Adapted from https://github.com/posquit0/Awesome-CV
        
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %     Configuration
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \documentclass[11pt, a4paper]{awesome-cv}
        
        %%% Override a directory location for fonts(default: 'fonts/')
        \\fontdir[fonts/]
        
        %%% Configure a directory location for sections
        \\newcommand*{\sectiondir}{resume/}
        
        %%% Override color
        \colorlet{awesome}{black}
        
        \\usepackage{import}
    """
    personal = f"""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %     Personal Data
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%% Essentials
        \\name{{}}{{{basic.get('name', '')}}}
        \\address{{{basic.get('address', '')}}}
        \mobile{{{basic.get('mobile', '')}}}
        %%% Social
        \email{{{basic.get('email', '')}}}
        \homepage{{{basic.get('homepage', '')}}}
        \github{{{basic.get('github', '')}}}
        \linkedin{{{basic.get('linkedin', '')}}}
    
    """
    body_and_footer = """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %     Content
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        \\begin{document}
        
        \makecvheader
        
        \import{\sectiondir}{education.tex}
        \\vspace{-0.4cm}
        \import{\sectiondir}{experience.tex}
        \\vspace{-0.4cm}
        \import{\sectiondir}{skills.tex}
        
        \end{document}

    """

    resume_tex = f"""
    {preamble}
    {personal}
    {body_and_footer}
    """

    return inspect.cleandoc(resume_tex)