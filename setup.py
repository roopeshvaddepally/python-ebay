from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='python-ebay',
      version=version,
      description="Python wrapper for eBay API",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ebay api wrapper',
      author='Roopesh Vaddepally',
      author_email='roopeshvaddepally@gmail.com',
      url='',
      license='',
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
