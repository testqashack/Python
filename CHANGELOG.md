# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Dynamic settings using constance
- User detail to be used by Dashboard app


### Changed

- Restructure user model
- Restructured admin interface
- UID fields changed from Char to UUID type

### Removed

-

## [v1.0.1] - 02-23-2018

### Added

- Added .env file for environment management
- Added logic for account management
- Added Celery for running periodic tasks
- Added REST framework for internal API
- Added Debug Toolbar for faster debugging
- Added simple logic for a line graph
- Added PACE.js to the frontend

### Changed

- Caching mechanism for fetching data from Grovestream
- Components tied to an Organisation
- Application tied to debug value
- Replaced d3.js with c3.js for faster development

### Removed

- Removed Heroku support