import click

from pyprofile.transformers import validyaml, texcv, website


@click.group()
def cli():
    pass


@cli.command()
def validate_and_concat():
    validyaml.generate.main('profile', False, 'profile-private.yml')
    validyaml.generate.main('profile', True, 'profile-public.yml')


@cli.command()
def generate_tex_cv():
    texcv.generate.main("profile-private.yml", "tex-cv-private")
    texcv.generate.main("profile-public.yml", "tex-cv-public")


@cli.command()
def generate_website():
    website.generate.main("profile-public.yml", "website")


# @cli.command()
# def generate_all():
#     validate_and_concat()
#     generate_tex_cv()
#     generate_website()


if __name__ == '__main__':
    cli()
