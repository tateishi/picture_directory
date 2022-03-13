from pathlib import Path

import yaml


def mkdir(path):
    path.mkdir(parents=True, exist_ok=True)


def fullpath(param, camera):
    return (
        Path(param['place']) /
        f'{param["year"]}年' / 
        f'{camera}_{param["date"]}_{param["event"]}'
    )


def load_param(path):
    with open(path, encoding='utf-8') as reader:
        return yaml.safe_load(reader)
