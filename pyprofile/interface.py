import click

from pyprofile.transformers import validyaml, texcv


# todo: command groups

@click.command()
@click.argument('profile_directory')
@click.option('--censored/--uncensored', '-p', default=True)
@click.option('--output', '-o')
def generate_validyaml(profile_directory, censored, output):
    validyaml.generate.main(profile_directory, censored, output)


@click.command()
@click.argument('profile_file')
@click.argument('resume_save_dir')
def generate_texcv(profile_file, resume_save_dir):
    texcv.generate.main(profile_file, resume_save_dir)
