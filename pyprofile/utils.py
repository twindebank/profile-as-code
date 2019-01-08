def recursively_replace_dict_str(d, orig, new):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = recursively_replace_dict_str(v, orig, new)
    elif isinstance(d, list):
        return [recursively_replace_dict_str(i, orig, new) for i in d]
    elif isinstance(d, str):
        return d.replace(orig, new)
    return d


def replace_none_with_str_recurs(any_dict):
    for k, v in any_dict.items():
        if v is None:
            any_dict[k] = ""
        elif isinstance(v, dict):
            replace_none_with_str_recurs(v)
        elif isinstance(v, list):
            for n, item in enumerate(v):
                if isinstance(item, dict):
                    replace_none_with_str_recurs(item)