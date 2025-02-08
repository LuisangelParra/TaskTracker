# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='TaskTracker',
    version='0.1.0',
    description='Task tracker is a project used to track and manage your tasks',
    author='Luisangel Parra',
    author_email='lfaria@uninorte.edu.co',
    url='https://github.com/LuisangelParra/TaskTracker',
    packages=find_packages(exclude=('Tests'))
)