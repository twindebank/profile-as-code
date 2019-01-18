import click

from pyprofile.transformers import validyaml, texcv, website
import click
import ast


# click

class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except Exception:
            raise click.BadParameter(value)


# implementations

def _validate_and_concat():
    validyaml.generate.main('profile', False, 'profile-private.yml')
    validyaml.generate.main('profile', True, 'profile-public.yml')


def _generate_tex_cv(exclude_experience=()):
    texcv.generate.main("profile-private.yml", "tex-cv-private", exclude_experience)
    texcv.generate.main("profile-public.yml", "tex-cv-public", exclude_experience)


def _generate_website():
    website.generate.main("profile-public.yml", "website")


# click wrapped

@click.group()
def cli():
    pass


@cli.command()
def validate_and_concat():
    _validate_and_concat()


@cli.command()
@click.option('--exclude-experience', default="[]", cls=PythonLiteralOption)
def generate_tex_cv(exclude_experience):
    _generate_tex_cv(exclude_experience)


@cli.command()
def generate_website():
    _generate_website()


@cli.command()
@click.option('--exclude-experience-cv', default="[]", cls=PythonLiteralOption)
def generate_all(exclude_experience_cv):
    _validate_and_concat()
    _generate_tex_cv(exclude_experience_cv)
    _generate_website()


if __name__ == '__main__':
    cli()
