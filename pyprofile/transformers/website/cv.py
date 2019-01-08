from dominate.tags import body, section, a, p, div, article, ul, li, span, b, br
from dominate.util import text


def generate_html(profile_info):
    html_body = body()
    with html_body:
        with section(_class="leading animated fadeInDown"):
            with a(href='/'):
                p(profile_info['basic_details']['name'], _class="leading-bigtext")
            p(profile_info['basic_details']['bio'][:-4], _class="leading-text")
        for section_title in ['education', 'experience']:
            with section(_class=f"cards animated fadeInUp {section_title}"):
                div(section_title, _class='section-title')
                roles = profile_info[section_title]
                for role in roles:
                    with article():
                        with div(_class='cventry'):
                            if section_title == "experience":
                                with div(_class='entry-header'):
                                    div(role['job_title'], _class='entry-title')
                                    div(f"{role['start_date']} - {role['end_date']}", _class='entry-date')
                                with div(_class="entry-subheader"):
                                    div(role['name']['long'], _class='entry-organisation')
                                    div(role['location'], _class='entry-location')
                                with div(_class='entry-body'):
                                    with ul():
                                        for para in role['description']['long']:
                                            li(para)

                            elif section_title == "education":
                                if role == "university":
                                    for university in profile_info[section_title][role]:
                                        with div(_class='entry-header'):
                                            div(university['institution'], _class='entry-title')
                                            div(f"{university['start_date']} - {university['end_date']}",
                                                _class='entry-date')
                                        with div(_class="entry-subheader"):
                                            div(university['course'], _class='entry-organisation')
                                            with div(_class='entry-location'):
                                                span(f"{university['degree']}, {university['classification']}")
                                        with div(_class='entry-body'):
                                            with ul():
                                                for para in university['achievements']:
                                                    li(para)
                                elif role == "school":
                                    for school in profile_info[section_title][role]:
                                        with div(_class='entry-header'):
                                            div(school['name'], _class='entry-title')
                                            div(f"{school['start_date']} - {school['end_date']}", _class='entry-date')

                                        with div(_class='entry-body'):
                                            a_levels = [f"{a_level['name']}: {a_level['grade']}" for a_level in
                                                 school['a_levels']]
                                            with ul():
                                                with li():
                                                    b("A-Levels:")
                                                    for a_level in a_levels:
                                                        br()
                                                        text(a_level)
                                            gcses = [f"{gcse['grade']}: {gcse['count']}" for gcse in
                                                               school['gcses']]
                                            with ul():
                                                with li():
                                                    b("GCSEs:")
                                                    for gcse in gcses:
                                                        br()
                                                        text(gcse)

                                else:
                                    raise ValueError(f"'{role}' is an invalid education type.")

        with section(_class="cards animated fadeInDown skills"):
            div('skills', _class='section-title')
            with article():
                for skill in profile_info['skills']:
                    div(skill['name'], _class='skill')

    return str(html_body)