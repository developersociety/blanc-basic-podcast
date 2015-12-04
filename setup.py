#!/usr/bin/env python
from codecs import open

from setuptools import find_packages, setup


with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='blanc-basic-podcast',
    version='0.2',
    description='Blanc Basic Podcast for Django',
    long_description=readme,
    url='https://github.com/blancltd/blanc-basic-podcast',
    maintainer='Blanc Ltd',
    maintainer_email='studio@blanc.ltd.uk',
    platforms=['any'],
    extras_require={
        ':python_version == "2.7"': [
            'hsaudiotag>=1.1.1',
        ],
        ':python_version >= "3.3"': [
            'hsaudiotag3k>=1.1.3',
        ],
    },
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    license='BSD',
)
