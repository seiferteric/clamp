from setuptools import setup, find_packages
import os

setup(
      name = "clamp",
      version = '0.0.1',
      #packages = find_packages(),
      author = "Eric Seifert",
      author_email = "seiferteric@gmail.com",
      description = "CLAMP CLI alias tool with variable substitution.",
      keywords = "CLI alias", 
      url = "https://github.com/seiferteric/clamp",
      zip_safe = True,
      scripts = ['clamp']



)
