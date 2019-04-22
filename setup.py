# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Cucumber Injector',
    version='0.0.1',
    description='''Joining the power of BDD and Data-Driven Testing
     in a lightweight command line tool written in Python''',
    long_description=readme,
    author='Joao Farias',
    author_email='jgfarias42@gmail.com',
    url='https://github.com/JoaoGFarias/CucumberInjector',
    license=license,
    packages=find_packages(
        exclude=(
            'tests',
            'docs',
            'sample')))
