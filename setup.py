# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TaskTracker',
    version='0.1.0',
    description='Task tracker is a project used to track and manage your tasks',
    long_description=readme,
    author='Luisangel Parra',
    author_email='lfaria@uninorte.edu.co',
    url='https://github.com/LuisangelParra/TaskTracker',
    license=license,
    packages=find_packages(exclude=('Tests')),
    entry_points={
        "console_scripts": [
            "task-cli=TaskTracker.task_cli:main", 
        ],
    },
)