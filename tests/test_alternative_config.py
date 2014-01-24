'''
Tests for functionality to use arbitrary configuration files.


Configuration
=============

This test script uses a custom configuration file ``config-test1.ini`` 
inside directory ``tests/``. It can be most easily created, by first copying::

     mv config-test1.ini.example  config-test1.ini
     
Then filling in user and application keys into ``config-test1.ini``.


Operation
=========

The test assumes the following directory layout::

    python-ebay/
        ebay/
            config.ini (optional, does'nt need to exist)
        tests/
            config-test1.ini
            config-test1.ini.example
            test_alternative_config.py

The test script creates a copy of the configuration file ``config.ini``: 

    ``config.ini.bak``
    
It can be used to restore the initialization file in case the original 
configuration file is lost.

The test itself never uses ``ebay/config.ini``, it always uses 
``tests/config-test1.ini`` for its configuration.
'''
import os
from os import path
import shutil
import unittest
from lxml import objectify

from ebay.utils import set_config_file
from ebay.shopping import GeteBayTime


def relative(*paths):
    "Create file paths that are relative to the location of this file."
    return path.abspath(path.join(path.dirname(__file__), *paths))


#File paths
std_conf = relative("../ebay/config.ini")
std_conf_back = relative("../ebay/config.ini.bak")
alt_conf = relative("config-test1.ini")
        

class TestAlternativeConfig(unittest.TestCase):

    def test_alternative_config(self):
        """
        Ensure the standard configuration file ``ebay/config.ini`` does not 
        exist, and try to use the library with the alternative configuration 
        file ``tests/config-test1.ini`.
        """
        #Copy original/standard configuration file to backup location
        shutil.copy(std_conf, std_conf_back)
        #Remove the standard configuration file
        os.remove(std_conf)
        
        #Look where the initialization files really are
        os.system("ls -l ../ebay/*.ini") #Should not exist
        os.system("ls -l ../tests/*.ini")
        
        #Set alternative initialization file
        set_config_file(alt_conf)
        
        #Use the library and test if it works
        result = GeteBayTime(encoding="XML")
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        ebay_time = root.Timestamp.text 
        print ebay_time
        self.assertTrue(len(ebay_time) > 10, 
                        "eBay time is a somewhat long string.")
        
        #Restore the original configuration file from the backup.
        shutil.copy(std_conf_back, std_conf)
 

    def test_regular_config(self):
        "Test the library with the regular configuration file."
        #Copy original/standard configuration file to backup location
        shutil.copy(std_conf, std_conf_back)
        #Remove the standard configuration file
        os.remove(std_conf)
        
        #Move the alternative configuration file to the standard location,
        #because we know that the alternative configuration file works.
        shutil.copy(alt_conf, std_conf)
        
        #Look where the initialization files really are
        os.system("ls -l ../ebay/*.ini")
        os.system("ls -l ../tests/*.ini")
        
        #Use the library and test if it works
        result = GeteBayTime(encoding="XML")
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        ebay_time = root.Timestamp.text 
        print ebay_time
        self.assertTrue(len(ebay_time) > 10, 
                        "eBay time is a somewhat long string.")
    
        #Restore the original configuration file from the backup.
        shutil.copy(std_conf_back, std_conf)


if __name__ == "__main__":
    #Run single test manually. 
#    t = TestAlternativeConfig("test_alternative_config")
#    t.test_alternative_config()

    unittest.main()
