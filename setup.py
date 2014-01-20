from setuptools import setup, find_packages
from os.path import join, dirname, abspath, isfile
from shutil import copy


def relative(*path_fragments):
    'Create a file path that is relative to the location of this file.'
    return abspath(join(dirname(abspath(__file__)), *path_fragments))

def read(fname):
    """
    Read a (text) file, and return its contents. 
    
    The file name must be relative to the location of this file.
    Used to put the contents of the README file into the library's 
    long_description below.
    """
    return open(relative(fname)).read()


#Create a dummy configuration file, if no configuration file exists.
#Otherwise there will installation errors that look ugly, 
#and may confuse users.
conf_file = relative('ebay/config.ini')
conf_example = relative('ebay/config.ini.example')
if not isfile(conf_file):
    copy(conf_example, conf_file)

#Start the setup machinery, give it detailed information about this library.
setup(name='python-ebay',
      version="0.2.0b5",
      description="Python Wrapper for eBay API",
      long_description=read('README.rst'),
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
      packages=['ebay'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "requests",
          "lxml"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      data_files=[('ebay', ['ebay/config.ini', 'ebay/config.ini.example'])],
)
