#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='blanc-basic-podcast',
    version='0.1',
    description='Blanc Basic Podcast for Django',
    long_description=open('README.rst').read(),
    url='http://www.blanctools.com/',
    maintainer='Alex Tomkins',
    maintainer_email='alex@hawkz.com',
    platforms=['any'],
    install_requires=[
        'hsaudiotag>=1.1.1',
    ],
    packages=[
        'blanc_basic_podcast',
        'blanc_basic_podcast.podcast',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='BSD-2',
)
