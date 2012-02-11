from os.path import join, dirname, abspath
import urllib2
from ConfigParser import ConfigParser

def get_endpoint_response(endpoint_name, operation_name, data, encoding, **headers):

    config_dict = get_config_value({ ("endpoints", endpoint_name) : "",
                    ("keys", "app_name") : "",
                    ("keys", "dev_name") : "",
                    ("keys", "cert_name") : "",
                    ("call", "siteid") : "",
                    ("call", "compatibility_level") : "", })
    
    
    endpoint = config_dict[("endpoints", endpoint_name)]
    app_name = config_dict[("keys", "app_name")]
    dev_name = config_dict[("keys", "dev_name")]
    cert_name = config_dict[("keys", "cert_name")]
    compatibility_level = config_dict[("call", "compatibility_level")]
    siteId = config_dict[("call", "siteid")]

    http_headers = { "X-EBAY-API-COMPATIBILITY-LEVEL" : compatibility_level,
                "X-EBAY-API-DEV-NAME" : dev_name,
                "X-EBAY-API-APP-NAME" : app_name,
                "X-EBAY-API-CERT-NAME": cert_name,
                "X-EBAY-API-CALL-NAME": operation_name,
                "X-EBAY-API-SITEID" : siteId,
                "Content-Type" : "text/xml" }

    http_headers.update(headers)

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)

def get_config_value(configTupleDict):
    """ configTupleDict should be a dictionary with a tuple key
    where the value will be filled by this function
    (i.e. configTupleDict = { ("section", "key") : "actual value from config goes here", }
    """
    if configTupleDict:
        config = ConfigParser()
        config.read(relative("config.ini"))
        #fill the dict of tuples
        for curItem in configTupleDict:
            configTupleDict[curItem] = config.get(curItem[0],curItem[1])
            

    return configTupleDict

class Value(object):
    def __init__(self,
                 number=None,
                 text=None,
                 url=None):
        self.number = number
        self.text = text
        self.url = url


class Specification(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class CompatibilityPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class ApplicationPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class SortOrder(object):
    def __init__(self, sortPriority, order, propertyName):
        self.sortPriority = sortPriority
        self.order = order
        self.propertyName = propertyName
