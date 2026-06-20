"""Behavioral tests for the list_reserve C extension's public API.

One test module per public function, covering its documented behavior and error
paths. Function-specific rationale lives in the corresponding test module.

Deliberately out of scope:
- Absolute over-allocation figures. CPython over-allocates list literals of 3+
  elements, so capacity expectations are derived via capacity()/shrink_to_fit()
  rather than hardcoded, keeping the suite valid across CPython 3.10-3.14.
- Non-CPython runtimes. The extension reads private PyListObject fields, so PyPy
  and free-threaded builds are not targeted.

Without tests/__init__.py, discovery collects zero tests yet exits 0 on CPython
3.10/3.11 (the no-tests failure exit code is 3.12+).
"""
