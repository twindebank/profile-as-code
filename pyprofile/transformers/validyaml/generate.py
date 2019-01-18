import logging

import ruamel.yaml as yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(profile, output):
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


class NoAliasDumper(yaml.RoundTripDumper):
    def ignore_aliases(self, _data):
        return True


if __name__ == '__main__':
    main()
