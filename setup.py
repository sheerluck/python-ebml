import os.path
import pickle
import platform
import sys

from pkg_resources import (
    normalize_path,
    working_set,
    add_activation_listener,
    require,
)
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.test import test as test_command

setup(
    name='python-ebml',
    version='3.1415',
    description='Implements well.',
    url='https://b.me',
    author='<a@b.me>',
    author_email='a@b.me',
    license='MIT',
    packages=find_packages(),
    setup_requires=[
    ],
    zip_safe=False,
    include_package_data=True,
    test_suite=None,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
      ],
    long_description="""Implements well."""
)
