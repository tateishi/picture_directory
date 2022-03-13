from pathlib import Path

import click

from .core import mkdir, load_param, fullpath


@click.command()
@click.option('--file', type=Path, required=True, help='parameter file.')
@click.option('--debug', is_flag=True)
@click.option('--verbose', is_flag=True)
def command(file: Path, debug: bool, verbose: bool):
    param = load_param(file)
    if verbose:
        click.echo(param)
    for camera in param['cameras']:
        directory = fullpath(param, camera)
        if verbose:
            click.echo(directory)
        if not debug:
            mkdir(directory)
