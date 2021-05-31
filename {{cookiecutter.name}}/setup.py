#!/usr/bin/env python

import pathlib

from typing import Dict

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Load the package's metadata from __version__.py
# Do not import it, because it will also import external dependencies which
# setup.py will install after processing
about: Dict[str, str] = {}
with (here / "{{cookiecutter.name}}" / "__version__.py").open() as f:
    exec(f.read(), about)

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name=about["__name__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    url=about["__url__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Typing :: Typed",
        "Programming Language :: Python :: {{cookiecutter.python_version}}",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
    ],
    keywords="algorithms, development",
    packages=find_packages(include=["{{cookiecutter.name}}", "{{cookiecutter.name}}.*"]),
    package_data={"": ["config.ini"]},
    python_requires="~={{cookiecutter.python_version}}",
    install_requires=[],
    project_urls={
        "Source": "{{cookiecutter.url}}",
    },
)
