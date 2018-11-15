from ruamel import yaml as yaml

from pyprofile.parsing import _recursively_replace_dict_str


def load_and_escape(path, special_chars=''):
    yaml_fd = open(path)
    yaml_profile = yaml.safe_load(
        yaml_fd
    )
    escaped = _escape_chars(yaml_profile, special_chars)
    yaml_fd.close()
    return escaped


def _escape_chars(dct, chars):
    for char in chars:
        dct = _recursively_replace_dict_str(dct, char, f"\\{char}")
    return dct