import yaml


def load(path):
    special_chars = '&%$#_{}~^\\'

    profile = yaml.load(open(path))

    for char in special_chars:
        profile = recursively_replace_dict_str(profile, char, f"\\{char}")

    return profile


def recursively_replace_dict_str(d, orig, new):
    for k, v in d.items():
        if k == 'achievements':
            print('hi')
        if isinstance(v, dict):
            d[k] = recursively_replace_dict_str(v, orig, new)
        elif isinstance(v, str):
            d[k] = v.replace(orig, new)
    return d
