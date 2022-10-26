from setuptools import setup, Extension


setup(ext_modules=[
          Extension("list_reserve", ["src/list_reserve.c"])
      ])
