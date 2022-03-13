from pathlib import Path


from .core import mkdir, load_param, fullpath


PARAMETER = Path('test/data/test1.yml')

def command():
    param = load_param(PARAMETER)
    print(param)
    for camera in param['cameras']:
        directory = fullpath(param, camera)
        print(directory)
#        mkdir(directory)


