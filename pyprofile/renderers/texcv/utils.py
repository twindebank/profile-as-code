def recursively_replace_dict_str(d, orig, new):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = recursively_replace_dict_str(v, orig, new)
    elif isinstance(d, list):
        return [recursively_replace_dict_str(i, orig, new) for i in d]
    elif isinstance(d, str):
        return d.replace(orig, new)
    return d


def recursively_censor_dict_strs(d, censor_with):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = recursively_censor_dict_strs(v, censor_with)
    elif isinstance(d, list):
        return [recursively_censor_dict_strs(v, censor_with) for v in d]
    elif isinstance(d, str) or isinstance(d, int):
        return censor_with
    return d
