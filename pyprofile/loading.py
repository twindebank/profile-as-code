from ruamel import yaml as yaml


def load_profile(path):
    yaml_fd = open(path)
    yaml_profile = yaml.safe_load(
        yaml_fd
    )
    yaml_fd.close()
    return yaml_profile
