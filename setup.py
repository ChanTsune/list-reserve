from setuptools import Extension, setup

# Project metadata is declared in pyproject.toml ([project]). setup.py only
# carries the C extension definition, which setuptools' declarative
# [tool.setuptools.ext-modules] table cannot yet express stably.
setup(
    ext_modules=[
        Extension("list_reserve._list_reserve", ["src/list_reserve.c"]),
    ],
)
