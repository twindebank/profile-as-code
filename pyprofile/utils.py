def recursively_replace_dict_str(d, orig, new):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = recursively_replace_dict_str(v, orig, new)
    elif isinstance(d, list):
        return [recursively_replace_dict_str(i, orig, new) for i in d]
    elif isinstance(d, str):
        return d.replace(orig, new)
    return d