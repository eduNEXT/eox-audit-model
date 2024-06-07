"""
Test Django settings for eox_audit_model project.
"""

from __future__ import unicode_literals

import codecs
import os

import yaml

from .common import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'eox_audit_model.apps.EoxAuditModelConfig',
]

TIME_ZONE = 'UTC'

# This key needs to be defined so that the check_apps_ready passes and the
# AppRegistry is loaded
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

ALLOW_EOX_AUDIT_MODEL = True
CELERY_TASK_ALWAYS_EAGER = False


def plugin_settings(settings):  # pylint: disable=function-redefined
    """
    For the platform tests
    """
    # setup the databases used in the tutor local environment
    if os.environ['LMS_CFG']:
        with codecs.open(os.environ['LMS_CFG'], encoding='utf-8') as f:
            env_tokens = yaml.safe_load(f)
        settings.DATABASES = env_tokens['DATABASES']
