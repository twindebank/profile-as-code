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
@click.argument('path')
@click.option('--censored/--uncensored', '-p', default=True)
@click.option('--output', '-o')
def validate_and_parse(censored, path, output):
    yaml_fd = open(path)
    yaml_profile = yaml.round_trip_load(
        yaml_fd,
        preserve_quotes=True
    )
    yaml_fd.close()

    if censored:
        yaml_profile = censor_profile(yaml_profile)

    del yaml_profile['private']

    yaml.round_trip_dump(
        yaml_profile,
        open(output, 'w'),
        default_flow_style=False,
        Dumper=MySD,
        indent=2,
        allow_unicode=True,
        explicit_start=True,
        explicit_end=True
    )


def censor_profile(profile):
    private = profile.get('private')
    for k in private:
        private[k] = '<CENSORED>'
    return profile


class MySD(yaml.RoundTripDumper):
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
    validate_and_parse()
