import click
from distutils.version import LooseVersion
import pkg_resources

import azk8sml
from azk8sml.cli.execute import execute
from azk8sml.cli.version import upgrade, version
from azk8sml.log import configure_logger

@click.group()
@click.option('-v', '--verbose', count=True, help='Turn on debug logging')
def cli(verbose):
    """
    Azure Kubernetes ML CLI interact`s with Kubernetes cluster on Azure and executes your commands.
    More help is available under each command listed below.
    """
    configure_logger(verbose)

def add_commands(cli):
    cli.add_command(execute)
    cli.add_command(version)

add_commands(cli)
