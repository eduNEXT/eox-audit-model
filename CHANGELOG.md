[0.7.0] - 2021-10-26

Added

- Tests for python 3.8.
- Compatibility notes to readme.


[0.6.0] - 2021-08-18

Added

- Support for batch requests. Handle lists in request data.
- Include new argument in decorator to show all the input parameters from the request.


[0.5.1] - 2021-07-16

Changed
- Handle lists in request data.


[0.5.0] - 2021-07-08

Added

- Display date in admin list view and use date format with ms
- Include an API wrapper to be used in API views to record the request data.
  Add an option to record sensitive data without the actual value.

[0.4.0] - 2021-05-24

Added

- Added support for django-ipware 3.0.0 .


[0.3.1] - 2021-05-18

Fixed

- Add missing parameters in celery task call.

[0.3.0] - 2021-04-29

Change

- The model is created asynchronously in order to avoid atomic blocks.

[0.2.1] - 2020-12-28

Fixed

- Changes made in AuditModel.
- Added missing migration.

[0.2.0] - 2020-10-23

Added

- Added support for Django 2.2.

[0.1.0] - 2020-08-18-

Added

- First release on PyPI.
