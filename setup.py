from setuptools import setup
import subprocess
ver = subprocess.check_output(["dpkg-parsechangelog", "-SVersion"]).strip().decode("utf-8", "strict")

setup(
      name = "clamp",
      version = ver,
      author = "Eric Seifert",
      author_email = "seiferteric@gmail.com",
      description = "CLAMP CLI alias tool with variable substitution.",
      keywords = "CLI alias", 
      url = "https://github.com/seiferteric/clamp",
      zip_safe = True,
      scripts = ['clamp'],
      extras_require = {
          'TAB_COMPLETE':  ["argcomplete", "TC"]
      }
)
