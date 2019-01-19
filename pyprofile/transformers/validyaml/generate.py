import logging
import os

import ruamel.yaml as yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(profile, output):
    _mkdir_if_not_exist(output)
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


def _mkdir_if_not_exist(output):
    if '/' in output:
        path = os.path.dirname(output)
        if not os.path.exists(path):
            os.makedirs(path)


class NoAliasDumper(yaml.RoundTripDumper):
    def ignore_aliases(self, _data):
        return True


if __name__ == '__main__':
    main()
