"""
Show how to use alternative configuration files.
"""
from os import system
from os.path import join, dirname, abspath

from ebay.utils import set_config_file
from ebay.finding import findItemsByKeywords


#Create file paths that are relative to the location of this file.
def relative(*paths):
    return abspath(join(dirname(abspath(__file__)), *paths))

#File paths
std_conf = relative("../ebay/config.ini")
alt_conf = relative("../config.apikey")

#Copy initialization file to nonstandard location
system("cp " + std_conf + " " + alt_conf)
#Look where the initialization files really are
system("ls " + std_conf)
system("ls " + alt_conf)

#Set alternative configuration file and use the library
set_config_file(alt_conf)
print findItemsByKeywords(keywords="ipod", encoding="XML", 
                          paginationInput = {"entriesPerPage": "5", 
                                             "pageNumber"    : "1"})
