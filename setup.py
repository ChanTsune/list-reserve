import os
from setuptools import setup, Extension

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(name='list_reserve',
      version='0.0.1',
      description='Python builtin list memory allocation library',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      ext_modules=[
        Extension('list_reserve', ['src/list_reserve.c'])],
      url='https://github.com/ChanTsune/list_reserve',
      author='ChanTsune',
      author_email='yshegou@gmail.com',
      license='MIT',
      keywords='list extension memory reserve capacity',
      )
