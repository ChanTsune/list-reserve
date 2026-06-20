# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Pre-built binary wheels on PyPI for CPython 3.8–3.14 across Linux
  (manylinux + musllinux; x86_64 and aarch64), Windows (AMD64 and ARM64), and
  macOS (x86_64 and arm64). Installing no longer requires a C compiler.
- Python 3.13 and 3.14 support.

### Removed
- Python 3.7 support (end of life).

## [0.3.2] - 2023-08-11

### Removed
- Python 3.5 and 3.6 support.

### Fixed
- C compiler warnings.

## [0.3.1] - 2021-12-15

### Added
- Python 3.10 support.

## [0.3.0] - 2020-11-25

### Added
- `allocated_bytes()` — return the list's allocated memory size.

## [0.2.0] - 2020-11-16

### Added
- Type hints (PEP 561 stub package).

## [0.1.1] - 2020-10-28

### Changed
- Improved docstrings and error messages.

## [0.1.0] - 2020-08-18

### Added
- `shrink_to_fit()` (#3).

## [0.0.1] - 2020-08-03

### Fixed
- `reserve()` (#1).

## [0.0.0] - 2020-08-02

### Added
- First release: `reserve()` and `capacity()`.

[Unreleased]: https://github.com/ChanTsune/list-reserve/compare/0.3.2...HEAD
[0.3.2]: https://github.com/ChanTsune/list-reserve/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/ChanTsune/list-reserve/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/ChanTsune/list-reserve/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/ChanTsune/list-reserve/compare/v0.1.1...0.2.0
[0.1.1]: https://github.com/ChanTsune/list-reserve/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/ChanTsune/list-reserve/compare/0.0.1...v0.1.0
[0.0.1]: https://github.com/ChanTsune/list-reserve/compare/0.0.0...0.0.1
[0.0.0]: https://github.com/ChanTsune/list-reserve/releases/tag/0.0.0
