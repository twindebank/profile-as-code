import glob

from ruamel import yaml as yaml


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def load_and_concat_raw_yaml(directory, file_pattern):
    filenames = sorted(glob.glob(f"{directory}/{file_pattern}"))

    separate = []
    for filename in filenames:
        with open(filename) as f:
            separate.append(f.read())
    concatenated = '\n'.join(separate)
    return yaml.safe_load(concatenated)
