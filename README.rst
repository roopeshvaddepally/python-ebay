=========================================
python-ebay - Python Wrapper for eBay API
=========================================

This project intends to create a simple python wrapper around eBay APIs.


Development and Download Sites
==============================

The entry at the *Python Package Index* is at: 
https://pypi.python.org/pypi/python-ebay

Development is coordinated at *Github*: 
https://github.com/roopeshvaddepally/python-ebay


How to Install
==============

New Way
-------

* Install the library with **pip** or **easy_install**. With *pip* you must 
  use option ``--pre``, because *python-ebay* is currently labeled as 
  prerelease (beta) quality. ::

        pip install --pre python-ebay
   
* Create a configuration file.
   * Generate keys at eBay's developer website: 
     http://developer.ebay.com/quickstartguide/
   * Create an example configuration file.
   * Rename the example to something sensible.
   * Edit the example, especially insert the keys that you generated at 
     eBay's developer site. 

* ::

        python -c "import ebay.utils; ebay.utils.write_config_example()"
        mv config.ini.example ebay.apikey
        vim ebay.apikey

* Before using *python-ebay*, you must tell it where the configuration file is::
     
        from ebay.utils import set_config_file
        from ebay.shopping import FindProducts

        set_config_file("ebay.apikey")
        print FindProducts("pen", "false", "10", "JSON")

Old Way
-------

* Download a source package of **python-ebay** and unpack it.
  https://github.com/roopeshvaddepally/python-ebay/tarball/master

* Create a configuration file.
   * Generate keys at eBay's developer website: 
     http://developer.ebay.com/quickstartguide/
   * Edit ``ebay/config.ini``, especially insert the keys that you generated at 
     eBay's developer site. 

* Install the (slightly modified) package with::

        python setup.py install

* The *python-ebay* library now contains a working configuration file. 
  You can use it without calling ``utils.set_config_file``::

        from ebay.shopping import FindProducts  
        print FindProducts("pen", "false", "10", "JSON")


Documentation
=============

The *pyton-ebay* library is unfortunately not complete. 
An overview of the development status is available on our wiki. 
The currently implemented functions are listed together with a short description:
https://github.com/roopeshvaddepally/python-ebay/wiki/List-of-eBay-APIs

Extensive documentation of eBay's API is available on eBay's developer website. 
This documentation focusses on XML messages that are sent to eBay's servers, 
and XML responses that are received from those servers.
http://developer.ebay.com/products/overview

Example code in Python can be found in the directories ``examples/`` and 
``tests/``. The complete source code can be obtained by either:

* Downloading an archive from:
  https://github.com/roopeshvaddepally/python-ebay/tarball/master
* Cloning the git repository::
    
        git clone git://github.com/roopeshvaddepally/python-ebay.git


License
=======

Apache License, Version 2.0
Please refer to details here: http://www.apache.org/licenses/LICENSE-2.0.html


Contributors
============

* Eike Welk  
* Utkarsh Sengar  
* Roopesh Vaddepally  
* Stephen Balaban  
* hbtronix  
* bogdanvarlamov  
* patoch  

