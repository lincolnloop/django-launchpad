#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = __import__('launchpad').__version__

setup(
    name="django-launchpad",
    version=VERSION,
    author='Peter Baumgartner',
    author_email='pete@lincolnloop.com',
    description=("Django application to collect an email list"),
    packages=find_packages(),
    package_data={'launchpad': [
        'templates/launchpad/*.html',
    ]},
    provides=['launchpad'],
    install_requires=['Django>=1.3'],
    url="http://github.com/lincolnloop/django-launchpad/",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
