"""
===============================================================================
Create a release of "python-ebay". Upload files and metadata to PyPi.
===============================================================================

This script can be used to automate the release of new versions of the
"python-ebay" library, but it should also serve as documentation for the 
somewhat complex release process.

The PyPi site for "python-ebay" is at:
   https://pypi.python.org/pypi/python-ebay

Usage
======

The script has several options.

At the beginning of the release process you might want to run::

    python release.py -s
    
This stores your PyPi user name and password in "~/.pypirc". This step is not
necessary to make releases, but is convenient if you need several attempts to 
get the release right. If user name and password are not stored in in 
"~/.pypirc" Python's upload machinery will ask for them.

To upload metadata and files to PyPi run::

    python release.py -u
    
To clean up after a release, run::
    
    python release.py -c
    
This option deletes the "~/.pypirc" file.
"""

import argparse
import getpass
import os
import os.path as path 
import textwrap
import shutil
import subprocess

def relative(*path_fragments):
    'Create a file path that is relative to the location of this file.'
    return path.abspath(path.join(path.dirname(__file__), *path_fragments))


#Parse the command line arguments of the release script
parser = argparse.ArgumentParser(description=
    'Upload a new version of "python-ebay" to PyPi.')

parser.add_argument('-s, --start', dest='start', action='store_true',
                    help='Start the release process. '
                         'Temporarily store password and user name for PyPi '
                         'in "~/.pypirc".')
parser.add_argument('-u, --upload', dest='upload', action='store_true',
                    help='Upload files and metadata to PyPi.')
parser.add_argument('-c, --cleanup', dest='cleanup', action='store_true',
                    help='Cleanup after the release. '
                         'Especially remove "~/.pypirc".')

args = parser.parse_args()


#Do some necessary computations and checks
homedir = path.expanduser("~")
pypirc_path = path.join(homedir, ".pypirc")
if path.exists(pypirc_path):
    print ('"~/.pypirc" file exists. '
           'Delete it with "release -c" when you are done.\n')


#Default action: display help message. ----------------------------------------
if not (args.start or args.upload or args.cleanup):
    print "No action selected. You must select at least one action/option.\n"
    parser.print_help()
    exit(0)


#Start the release process ----------------------------------------------------
if args.start:
    #Create a ".pypirc" file 
    print 'Store PyPi username and password temporarily in "~/.pypirc" file.'
    username = raw_input("PyPi username:")
    password = getpass.getpass('PyPi password:')
    pypirc_text = textwrap.dedent(
        """
        [distutils]
        index-servers =
            pypi
        
        [pypi]
        repository: http://www.python.org/pypi
        username: {u}
        password: {p}
        """.format(u=username, p=password))
    with open(pypirc_path, "w") as pypirc_file:
        pypirc_file.write(pypirc_text)
        
    #Remind of necessary actions, that are easily forgotten. 
    print '\n=============================================='
    print "* Don't forget to increase the version."
    print '* Please run the tests before uploading a release!'
    print '============================================\n'
    #TODO: In the future, if tests really work, run the test suite.


#Do the release ---------------------------------------------------------------
if args.upload:
    #Delete the "config.ini" file, because it contains secrets.
    config_ini_path = relative("ebay/config.ini")
    if path.exists(config_ini_path):
        #Backup the "config.ini" file, if it exists.
        for i in range(1000):
            config_bak_path = config_ini_path + ".{}.bak".format(i)
            if not path.exists(config_bak_path):
                break
        shutil.copy(config_ini_path, config_bak_path)
        #Delete "config.ini" 
        os.remove(config_ini_path)
        
    #Build source distribution, upload metadata, upload distribution(s)
    subprocess.call(["python", "setup.py",
                     "sdist", 
                     "register", "-r", "pypi", 
                     "upload", "-r", "pypi",])


#Clean up from the release process. -------------------------------------------
if args.cleanup:
    #Remove the ".pypirc" file.
    if path.exists(pypirc_path):
        print 'Removing "~/.pypirc".'
        os.remove(pypirc_path)
    else:
        print 'Nothing to do.'
