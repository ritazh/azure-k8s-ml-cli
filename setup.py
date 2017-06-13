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
    ],
    setup_requires=[
    ],
    dependency_links=[
    ],
    entry_points={
        "console_scripts": [
            "azk8sml = azk8sml.main:cli",
        ],
    },
    tests_require=[
    ],
)
