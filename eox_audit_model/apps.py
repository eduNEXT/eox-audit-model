"""
App configuration for eox_audit_model.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EoxAuditModelConfig(AppConfig):
    """
    Django eduNEXT audit Model configuration.
    """
    name = 'eox_audit_model'
    verbose_name = 'Django eduNEXT Audit Model'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'production': {'relative_path': 'settings.production'},
                'devstack': {'relative_path': 'settings.devstack'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
