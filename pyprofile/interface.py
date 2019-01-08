import logging

import click

from pyprofile.transformers import validyaml, texcv


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


if __name__ == '__main__':
    cli()
