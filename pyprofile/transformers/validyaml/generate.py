import glob
import logging

import ruamel.yaml as yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(profile_directory, censored, output):
    logger.info(f"Loading profile from '{profile_directory}' and generating '{output}'")
    public_yaml = _load_and_concat_raw_yaml(profile_directory, '*.yml')
    private_yaml = _load_and_concat_raw_yaml(profile_directory, '.*.yml')

    if censored:
        private_yaml = _censor_private_raw_yaml(private_yaml)

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
    logger.info(f"Output saved to '{output}'")


def _load_and_concat_raw_yaml(directory, file_pattern):
    filenames = sorted(glob.glob(f"{directory}/{file_pattern}"))
    concatenated = '\n'.join([open(f).read() for f in filenames])
    return concatenated


def _censor_private_raw_yaml(private_yaml):
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


if __name__ == '__main__':
    main()
