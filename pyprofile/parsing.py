import glob
import io

import click
import ruamel.yaml as yaml


def load(path, special_chars=''):
    yaml_fd = open(path)
    yaml_profile = yaml.safe_load(
        yaml_fd
    )
    escaped = _escape_chars(yaml_profile, special_chars)
    yaml_fd.close()
    return escaped


@click.command()
@click.argument('profile_directory')
@click.option('--censored/--uncensored', '-p', default=True)
@click.option('--output', '-o')
def validate_and_parse_profile(profile_directory, censored, output):
    public_yaml_filenames = sorted(glob.glob(f"{profile_directory}/*.yml"))
    public_yaml = '\n'.join([open(f).read() for f in public_yaml_filenames])

    private_yaml_filenames = glob.glob(f"{profile_directory}/.*.yml")
    private_yaml = '\n'.join([open(f).read() for f in private_yaml_filenames])

    if censored:
        private_yaml = censor_private_yaml(private_yaml)

    profile_yaml = ''.join([private_yaml, public_yaml])

    yaml_profile = yaml.round_trip_load(
        profile_yaml,
        preserve_quotes=True
    )

    del yaml_profile['private']

    yaml.round_trip_dump(
        yaml_profile,
        open(output, 'w'),
        default_flow_style=False,
        Dumper=NoAliasDumper,
        indent=2,
        allow_unicode=True,
        explicit_start=True,
        explicit_end=True
    )


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


def _escape_chars(dct, chars):
    for char in chars:
        dct = _recursively_replace_dict_str(dct, char, f"\\{char}")
    return dct


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
