#!/usr/bin/env python
import os
from setuptools import find_packages, setup

project = "azure-k8s-ml-cli"
version = "0.1.0"

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
    name=project,
    version=version,
    description="Command line tool for Azure Kubernetes ML",
    long_description=long_description,
    author="Microsoft",
    author_email="ritazh@microsoft.com",
    url="https://github.com/ritazh/azure-k8s-ml-cli",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    keywords="Azure Kubernetes ML",
    install_requires=[
        "click>=6.7",
        "clint>=0.5.1",
        "requests>=2.12.4",
        "requests-toolbelt>=0.7.1",
        "marshmallow>=2.11.1",
        "pytz>=2016.10",
        "shortuuid>=0.4.3",
        "tabulate>=0.7.7",
        "pathlib2>=2.2.1",
        "backports.tempfile>=1.0rc1",
        "backports.weakref>=1.0rc1",
    ],
    setup_requires=[
        "nose>=1.0",
    ],
    dependency_links=[
    ],
    entry_points={
        "console_scripts": [
            "azk8sml = azk8sml.main:cli",
        ],
    },
    tests_require=[
        "nose>=1.0",
        "mock>=1.0.1",
    ],
)
