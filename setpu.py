from setuptools import setup, Extension
 
setup(name = 'list_reserve',
      version = '0.0.0',
      ext_modules = [
         Extension('list_reserve', ['c_source/list_reserve.c'])]
      )
