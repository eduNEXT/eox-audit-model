==========================
Django edunext audit model
==========================

|Maintainance Badge| |Test Badge| |PyPI Badge|

.. |Maintainance Badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
   :alt: Maintainance Status
.. |Test Badge| image:: https://img.shields.io/github/actions/workflow/status/edunext/eox-audit-model/.github%2Fworkflows%2Ftests.yml?label=Test
   :alt: GitHub Actions Workflow Test Status
.. |PyPI Badge| image:: https://img.shields.io/pypi/v/eox-audit-model?label=PyPI
   :alt: PyPI - Version
   
Eox audit model is a Django application that provides an audit model for tracking and logging changes within the Open edX platform.
This plugin is designed to help administrators and developers maintain a comprehensive audit trail of various operations, ensuring better monitoring.

Features
========

- Tracks changes to specified models.
- Logs detailed information about create, update, and delete operations.

Installation
============

1. Install eox-audit-model:

    .. code-block:: python

      pip install eox-audit-model

2. Add “eox_audit_model” to your INSTALLED_APPS:

    .. code-block:: python

      INSTALLED_APPS = [
              ...
            'eox_audit_model',
      ]

3. Run Migrate:

    .. code-block:: python

      python manage.py migrate eox_audit_model


Open edX compatibility notes
----------------------------

+------------------+---------------+
| Open edX Release | Version       |
+==================+===============+
| Juniper          | >=0.2, < 0.4  |
+------------------+---------------+
| Koa              | >=0.4, <= 0.7 |
+------------------+---------------+
| Lilac            | >=0.4, <= 0.7 |
+------------------+---------------+
| Maple            | >=0.7, <1.0   |
+------------------+---------------+
| Nutmeg           | >=1.0         |
+------------------+---------------+
| Olive            | >=2.0         |
+------------------+---------------+
| Palm             | >=3.0         |
+------------------+---------------+
| Quince           | >=4.0         |
+------------------+---------------+
| Redwood          | >=4.2.0       |
+------------------+---------------+


Usage
=====

Audit any execution of a method or function. This will create a database register with the following information:

#. **Status**: If the process was successful or not.
#. **Action**: The given string to identify the process.
#. **Timestamp**: The execute date.
#. **Method name**: Method or function name.
#. **Captured log**: Logs generated in the execution.
#. **Traceback log**: If there is an exception, this will contain the traceback.
#. **Site**: Current site.
#. **Performer**: The user who started the method; depends on the *request.user*.
#. **Input**: The values used to execute the method.
#. **Output**: The value returned by the method.
#. **Ip**: Current IP.

- Example:

.. code-block:: python

  from eox_audit_model.models import AuditModel

  def any_method(parameter1, parameter2, parameter3):
    """Do something"""
    return 'Success'

  def audit_process():
    """Execute audit process"""
    action = "This is a simple action"
    parameters = {
      "args": (2, 6),
      "kwargs": {"parameter3": 9},
    }

    expected_value = AuditModel.execute_action(action, any_method, parameters)
    ...

Decorator
---------
There is a simple decorator, which can perform the same process.

- Example:

.. code-block:: python

  from eox_audit_model.decorators import audit_method

  @audit_method(action="This is a simple action")
  def any_method(parameter1, parameter2, parameter3):
    """Do something"""
    return 'Success'

  def audit_process():
    """Execute audit process"""
    expected_value = any_method(3, 6, 9)
    ...

License
=======

This software is licensed under the terms of the AGPLv3. See the LICENSE file for details.
