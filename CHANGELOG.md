# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v4.1.0 - 2024-03-19

### [4.1.0](https://github.com/eduNEXT/eox-audit-model/compare/v4.0.0...v4.1.0) (2024-03-19)

#### Features

* add workflow to add items to the Dedalo project DS-831 ([#29](https://github.com/eduNEXT/eox-audit-model/issues/29)) ([4ca38ca](https://github.com/eduNEXT/eox-audit-model/commit/4ca38cafeda4941ff755685d8258c24895ceb28f))

## v4.0.0 - 2024-02-13

### [4.0.0](https://github.com/eduNEXT/eox-audit-model/compare/v3.1.0...v4.0.0) (2024-02-13)

#### ⚠ BREAKING CHANGES

* add compatibility with quince release
  
* perf: update requirements and readme
  
* perf: update requirements
  
* perf: update requirements
  
* perf: update requirements
  
* perf: update labeler version
  
* fix: update actions/setup-python version
  

#### Performance Improvements

* quince release support ([#28](https://github.com/eduNEXT/eox-audit-model/issues/28)) ([62a9b3e](https://github.com/eduNEXT/eox-audit-model/commit/62a9b3ef1e9ab38848a020dc677f1e23f479c197))

## v3.1.0 - 2024-01-12

### [3.1.0](https://github.com/eduNEXT/eox-audit-model/compare/v3.0.0...v3.1.0) (2024-01-12)

#### Features

* add absolute uri to djrf-api audit decorator ([#25](https://github.com/eduNEXT/eox-audit-model/issues/25)) ([ed001ac](https://github.com/eduNEXT/eox-audit-model/commit/ed001acb67c451a0fee364d826a4abed2043b0a5))

## v3.0.0 - 2023-12-15

### [3.0.0](https://github.com/eduNEXT/eox-audit-model/compare/v2.0.0...v3.0.0) (2023-12-15)

#### ⚠ BREAKING CHANGES

* add compatibility with palm release
  
* ci: update dependencies of GitHub actions
  
* docs: update readme file
  
* fix: message_control wasn't being used
  
* refactor: allow 120 characters per line when Pylint is executed
  
* refactor:  fix Pylint warnings
  
* chore: update requirements
  

#### Performance Improvements

* add compatibility with palm release ([#27](https://github.com/eduNEXT/eox-audit-model/issues/27)) ([c4bff09](https://github.com/eduNEXT/eox-audit-model/commit/c4bff09c739ea9476f8bb803a21d40a49727ed4b))

#### Documentation

* adds status label to readme file ([462061c](https://github.com/eduNEXT/eox-audit-model/commit/462061c9bf9e6cae27dc6c7305aa1c50bae28c1b))

## v2.0.0 - 2023-01-27

### [2.0.0](https://github.com/eduNEXT/eox-audit-model/compare/v1.0.0...v2.0.0) (2023-01-27)

#### ⚠ BREAKING CHANGES

- **DS-368:** add compatibility with olive

#### Performance Improvements

- **DS-368:** add support for olive Open edX release ([#24](https://github.com/eduNEXT/eox-audit-model/issues/24)) ([e4b6e4c](https://github.com/eduNEXT/eox-audit-model/commit/e4b6e4cae097aa769435fd40342964a1d120ebca))

#### Continuous Integration

- adds mantainer group ([64e8904](https://github.com/eduNEXT/eox-audit-model/commit/64e8904c13683846a8f432de484ffbcedb0bc4ea))
- update the changelog updater step in bumpversion ([#21](https://github.com/eduNEXT/eox-audit-model/issues/21)) ([92ee961](https://github.com/eduNEXT/eox-audit-model/commit/92ee96127ed31972b2a3353e153ab604d6bdea81))

## v1.0.0 - 2022-10-03

### [1.0.0](https://github.com/eduNEXT/eox-audit-model/compare/v0.7.3...v1.0.0) (2022-10-03)

#### ⚠ BREAKING CHANGES

- Drop Django 2.2 and python 3.5 compatibilities.

#### Features

- make eox-audit-model comptatible with nutmeg ([555fdfe](https://github.com/eduNEXT/eox-audit-model/commit/555fdfe609824990b72ee925225797ab91e0b0ab))
- update test suite workflow ([d4460cd](https://github.com/eduNEXT/eox-audit-model/commit/d4460cd33b28d8fcd6029988929cb25c92e49dba))

#### Bug Fixes

- add DEFAULT_AUTO_FIELD for primary keys ([139af1f](https://github.com/eduNEXT/eox-audit-model/commit/139af1f99f200b73c7253992d1d3167e7d564381))

#### Continuous Integration

- add workflow to publish python package ([6363938](https://github.com/eduNEXT/eox-audit-model/commit/6363938a447da14ee3b5541e3c8049f708970575))

#### Documentation

- uodate README compatibility notes ([5a1db6d](https://github.com/eduNEXT/eox-audit-model/commit/5a1db6d7b7004cc7b0b6dfcf673f0cf449e536c1))
- update readme github actions badges ([906faa1](https://github.com/eduNEXT/eox-audit-model/commit/906faa1ddecc0993cd1780ea8e80463a7666ba9b))

#### Code Refactoring

- remove code used with django-ipwere<3.0 ([1d0fb39](https://github.com/eduNEXT/eox-audit-model/commit/1d0fb3908747dced99f284c88755fe51e043437d))

#### Styles

- **pylint:** update disable rules and update makefile quality command ([1ef60ba](https://github.com/eduNEXT/eox-audit-model/commit/1ef60ba46ea64d8408927ca17011cbe24a5c2869))

## [0.7.0] - 2021-10-26

### Added

- Tests for python 3.8.
- Compatibility notes to readme.

## [0.6.0] - 2021-08-18

### Added

- Support for batch requests. Handle lists in request data.
- Include new argument in decorator to show all the input parameters from the request.

## [0.5.1] - 2021-07-16

### Change

- Handle lists in request data.

## [0.5.0] - 2021-07-08

### Added

- Display date in admin list view and use date format with ms
- Include an API wrapper to be used in API views to record the request data.
- Add an option to record sensitive data without the actual value.

## [0.4.0] - 2021-05-24

### Added

- Added support for django-ipware 3.0.0 .

## [0.3.1] - 2021-05-18

### Fixed

- Add missing parameters in celery task call.

## [0.3.0] - 2021-04-29

## Change

- The model is created asynchronously in order to avoid atomic blocks.

## [0.2.1] - 2020-12-28

### Fixed

- Changes made in AuditModel.
- Added missing migration.

## [0.2.0] - 2020-10-23

### Added

- Added support for Django 2.2.

## [0.1.0] - 2020-08-18-

### Added

- First release on PyPI.
