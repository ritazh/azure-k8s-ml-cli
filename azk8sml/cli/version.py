import pip
import pkg_resources
import click

from azk8sml.log import logger as azk8sml_logger


PROJECT_NAME = "azure-k8s-ml-cli"


@click.command()
def version():
    """
    Prints the current version of the CLI
    """
    version = pkg_resources.require(PROJECT_NAME)[0].version
    azk8sml_logger.info(version)


@click.command()
def upgrade():
    """
    Upgrade azure-k8s-ml command line
    """
    try:
        pip.main(["install", "--upgrade", PROJECT_NAME])
    except Exception as e:
        azk8sml_logger.error(e)
