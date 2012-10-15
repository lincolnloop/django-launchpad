django-launchpad
================

.. image:: https://secure.travis-ci.org/lincolnloop/django-launchpad.png
    :target: http://travis-ci.org/lincolnloop/django-launchpad

A simple application to track mailing list signups and unsubscribes. Useful for pre-launch signup pages.

Installation
------------

This isn't on PyPI (yet), nor is its dependency::

    pip install -e git+https://github.com/lincolnloop/django-jsonit.git#egg=jsonit
    pip install -e git+https://github.com/lincolnloop/django-launchpad.git#egg=launchpad

Configuration
-------------

Add ``launchpad`` to your ``INSTALLED_APPS`` and include ``launchpad.urls`` in your urlconf.

Templates are provided in the ``launchpad/templates/launchpad`` directory as an example. You'll want to create your own.

Tests
-----

Example settings are provided. Run this from the repo root::

    django-admin.py test --pythonpath=. --settings=example_settings