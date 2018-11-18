import os

import click
from dominate.tags import body, section, p, div, article, i, span, a, ul, li
from ruamel import yaml



@click.command()
@click.argument('profile_file')
@click.argument('resume_save_dir')
def generate_html(profile_file, resume_save_dir):
    html_body = body()
    with html_body:
        with section(_class="leading animated fadeInDown"):
            with a(href='/'):
                p(profile_info['personal_info']['name'], _class="leading-bigtext")
            p(profile_info['personal_info']['summary'][:-4], _class="leading-text")
        for section_title in ['education', 'jobs', 'volunteering']:
            with section(_class=f"cards animated fadeInUp {section_title}"):
                div(section_title, _class='section-title')
                roles = profile_info['experiences'][section_title]
                for role in roles:
                    if len(set(role.values())) > 1:
                        with article():
                            with div(_class='cventry'):
                                if section_title == "jobs":
                                    with div(_class='entry-header'):
                                        div(role['title'], _class='entry-title')
                                        div(role['date_range'], _class='entry-date')
                                    with div(_class="entry-subheader"):
                                        div(role['company'], _class='entry-organisation')
                                        div(role['location'], _class='entry-location')
                                    with div(_class='entry-body'):
                                        split = role['description'].split('- ')
                                        if len(split) > 1:
                                            with ul():
                                                for para in split[1:]:
                                                    li(para)
                                        else:
                                            p(role['description'])

                                elif section_title == "education":
                                    with div(_class='entry-header'):
                                        div(role['name'], _class='entry-title')
                                        div(role['date_range'], _class='entry-date')
                                    with div(_class="entry-subheader"):
                                        div(role['field_of_study'], _class='entry-organisation')
                                        with div(_class='entry-location'):
                                            span(role['degree'])
                                            if role['grades'] != '' and role['degree'] != '':
                                                span(', ')
                                            i(f"{role['grades']}", style="font-weight:300")
                                    with div(_class='entry-body'):
                                        split = role['description'].split('- ')
                                        if len(split) > 1:
                                            with ul():
                                                for para in split[1:]:
                                                    li(para)
                                        else:
                                            p(role['description'])
                                elif section_title == "volunteering":
                                    with div(_class='entry-header'):
                                        div(role['title'], _class='entry-title')
                                        div(role['date_range'], _class='entry-date')
                                    with div(_class="entry-subheader"):
                                        div(role['company'], _class='entry-organisation')
                                        # div(role['cause'], _class='entry-location')
                                    with div(_class='entry-body'):
                                        split = role['description'].split('- ')
                                        if len(split) > 1:
                                            with ul():
                                                for para in split[1:]:
                                                    li(para)
                                        else:
                                            p(role['description'])
        with section(_class="cards animated fadeInDown skills"):
            div('skills', _class='section-title')
            with article():
                for skill in profile_info['skills']:
                    div(skill['name'], _class='skill')

    return str(html_body)


def load_profile(path):
    yaml_fd = open(path)
    yaml_profile = yaml.safe_load(
        yaml_fd
    )
    yaml_fd.close()
    return yaml_profile


def set_up_html_dir(tex_dir):
    if not os.path.exists(tex_dir):
        os.makedirs(tex_dir)
    os.system(f"cp -r pyprofile/transformers/texcv/_tex_resources/* {tex_dir}/")


def save_html(html, filename):
    cv_body_file = open(filename, "w")
    cv_body_file.write(html)
    cv_body_file.close()


def replace_none_with_str_recurs(any_dict):
    for k, v in any_dict.items():
        if v is None:
            any_dict[k] = ""
        elif isinstance(v, dict):
            replace_none_with_str_recurs(v)
        elif isinstance(v, list):
            for n, item in enumerate(v):
                if isinstance(item, dict):
                    replace_none_with_str_recurs(item)


def main():
    LI_AT = os.getenv('LI_AT')
    profile_info = scrape_profile(LI_AT)
    # profile_info = json.load(open('profile.json'))
    html = profile_to_html(profile_info)
    save_html(html, "cv-body.html")


if __name__ == '__main__':
    main()
