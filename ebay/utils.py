from os.path import join, dirname, abspath
import urllib2
from ConfigParser import ConfigParser

def get_endpoint_response(endpoint_name, operation_name, data, encoding, **headers):
    config = ConfigParser()
    config.read(relative("config.ini"))
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", endpoint_name)

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-APPNAME": app_name,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)


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
