#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="sashay",
    install_requires=[
        "quo>=2022.5",
    ],
    package_data={
        # If any package contains *.txt files, include them:
        "sashay": ["assets/*.json"]},
)
