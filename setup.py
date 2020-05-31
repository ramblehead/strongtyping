#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.04.20
@author: felix
"""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name="strong-typing",
    version="1.0.0",
    description="Decorator which checks whether the function is called with the correct type of parameters",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/FelixTheC/strongtyping",
    author="FelixTheC",
    author_email="fberndt87@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    scripts=['strong_typing.py'],
    include_package_data=True,
    install_requires=[
        'attrs',
        'more-itertools',
        'packaging',
        'pluggy',
        'py',
        'pyparsing',
        'pytest',
        'six',
        'wcwidth'
    ],
)