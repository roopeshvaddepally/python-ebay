'''
Tests for functionality to use arbitrary configuration files.

The standard configuration file is part of the library itself. This is 
acceptable for web applications, but impossible for interactive programs.
For interactive program each user needs a separate configuration file. 

The test assumes the following directory layout::

    python-ebay/
        ebay/
            config.ini
        tests/
            test_alternative_config.py

The test script creates a copy of the initialization file: 

    ``config.ini.bak``
    
It can be used to restore the initialization file in case the original 
configuration file is lost.
'''
from os import system
from os.path import join, dirname, abspath
import unittest
from lxml import etree

from ebay.utils import set_config_file
from ebay.finding import findItemsByKeywords


def relative(*paths):
    "Create file paths that are relative to the location of this file."
    return abspath(join(dirname(abspath(__file__)), *paths))


#Arguments for `ebay.finding.findItemsByKeywords`
keywords = "ipod"
paginationInput = {"entriesPerPage": "5", "pageNumber" : "1"}
encoding = "XML"
#File paths
std_conf = relative("../ebay/config.ini")
std_conf_back = relative("../ebay/config.ini.bak")
alt_conf = relative("../config.apikey")
        

class TestAlternativeConfig(unittest.TestCase):

    def test_alternative_config(self):
        """
        Move configuration file ``config.ini`` to nonstandard location (one level
        up in directory hierarchy) and try to use the library.
        """
        #Backup the initialization file
        system("cp " + std_conf + " " + std_conf_back)
        #Move initialization file to nonstandard location
        system("mv " + std_conf + " " + alt_conf)
        #Look where the initialization files really are
        system("ls " + std_conf)
        system("ls " + std_conf_back)
        system("ls " + alt_conf)
        
        #Set alternative initialization file
        set_config_file(alt_conf)
        
        #Use the library and test if it works
        result = findItemsByKeywords(keywords=keywords, 
                                     paginationInput=paginationInput,
                                     encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        
        #Move initialization file back to original location
        system("mv " + alt_conf + " " + std_conf)
 

    def test_regular_config(self):
        "Test the library with the regular configuration file."
        #Look where the initialization files really are
        system("ls " + std_conf)
        system("ls " + std_conf_back)
        system("ls " + alt_conf)      #should not exist
        
        #Use the library and test if it works
        result = findItemsByKeywords(keywords=keywords, 
                                     paginationInput=paginationInput,
                                     encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
    


if __name__ == "__main__":
    #Run single test manually. 
#    t = TestAlternativeConfig("test_alternative_config")
#    t.test_alternative_config()

    unittest.main()
