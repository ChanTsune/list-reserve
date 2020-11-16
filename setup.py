import os
from setuptools import setup, Extension

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(name="list_reserve",
      version="0.2.0",
      description="Python builtin list memory allocation library",
      long_description=read("README.md"),
      long_description_content_type="text/markdown",
      packages=["list_reserve"],
      package_data={"list_reserve": ["py.typed", "__init__.pyi"]},
      ext_modules=[
        Extension("list_reserve", ["src/list_reserve.c"])],
      url="https://github.com/ChanTsune/list-reserve",
      author="ChanTsune",
      author_email="yshegou@gmail.com",
      license="MIT",
      keywords="list extension memory reserve capacity",
      )
