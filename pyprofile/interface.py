import click

from pyprofile.transformers import validyaml, texcv, website


# implementations

def _validate_and_concat():
    validyaml.generate.main('profile', False, 'profile-private.yml')
    validyaml.generate.main('profile', True, 'profile-public.yml')


def _generate_tex_cv():
    texcv.generate.main("profile-private.yml", "tex-cv-private")
    texcv.generate.main("profile-public.yml", "tex-cv-public")


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
def generate_tex_cv():
    _generate_tex_cv()


@cli.command()
def generate_website():
    _generate_website()


@cli.command()
def generate_all():
    _validate_and_concat()
    _generate_tex_cv()
    _generate_website()


if __name__ == '__main__':
    cli()
