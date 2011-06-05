from setuptools import setup, find_packages
import sys, os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(name='python-ebay',
      version="0.1",
      description="Python Wrapper for eBay API",
      long_description=read('README.md'),
      classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: Apache Software License",
    ],
      keywords='ebay api wrapper',
      author='Utkarsh Sengar, Roopesh Vaddepally',
      author_email='utkarsh2012@gmail.com, roopeshvaddepally@gmail.com',
      url='https://github.com/roopeshvaddepally/python-ebay',
      license='Apache Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "requests",
          "lxml"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
