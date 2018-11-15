import glob

import click
import ruamel.yaml as yaml


@click.command()
@click.argument('profile_directory')
@click.option('--censored/--uncensored', '-p', default=True)
@click.option('--output', '-o')
def validate_and_parse_profile(profile_directory, censored, output):
    public_yaml = load_and_concat_yaml(profile_directory, '*.yml')
    private_yaml = load_and_concat_yaml(profile_directory, '.*.yml')

    if censored:
        private_yaml = censor_private_yaml(private_yaml)

    profile_yaml = '\n'.join([private_yaml, public_yaml])

    profile = yaml.round_trip_load(
        profile_yaml,
        preserve_quotes=True
    )

    del profile['private']

    yaml.round_trip_dump(
        profile,
        open(output, 'w'),
        default_flow_style=False,
        Dumper=NoAliasDumper,
        indent=2,
        allow_unicode=True,
        explicit_start=True,
        explicit_end=True
    )


def load_and_concat_yaml(directory, file_pattern):
    filenames = sorted(glob.glob(f"{directory}/{file_pattern}"))
    concatenated = '\n'.join([open(f).read() for f in filenames])
    return concatenated


def censor_private_yaml(private_yaml):
    """Have to censor manually as loading in yaml fucks with aliases/anchors"""
    lines = private_yaml.split('\n')
    censored_lines = []
    for line in lines[1:]:
        if line:
            key, anchor_and_val = line.split('&')
            anchor, *_ = anchor_and_val.split(' ')
            censored_line = f"{key}&{anchor} <CENSORED>"
            censored_lines.append(censored_line)
    censored_lines.insert(0, lines[0])
    censored_yaml = '\n'.join(censored_lines)

    return censored_yaml


class NoAliasDumper(yaml.RoundTripDumper):
    def ignore_aliases(self, _data):
        return True


def _recursively_replace_dict_str(d, orig, new):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = _recursively_replace_dict_str(v, orig, new)
    elif isinstance(d, list):
        return [_recursively_replace_dict_str(i, orig, new) for i in d]
    elif isinstance(d, str):
        return d.replace(orig, new)
    return d


if __name__ == '__main__':
    validate_and_parse_profile()
