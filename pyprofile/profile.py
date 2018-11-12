import yaml


def load(path, special_chars=''):
    profile = _escape_chars(yaml.load(open(path)), special_chars)

    return profile


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
