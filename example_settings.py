"""Bare-bones settings to test launchpad"""
import os
from django.conf.urls.defaults import patterns, include

directory = os.path.dirname(__file__)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(directory, 'launchpad_example.db')
    }
}
filepath, extension = os.path.splitext(__file__)
ROOT_URLCONF = os.path.basename(filepath)
INSTALLED_APPS = ('launchpad',)
DEBUG=True

urlpatterns = patterns('', (r'', include('launchpad.urls')))
