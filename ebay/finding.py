import urllib2
from lxml import etree

from ConfigParser import ConfigParser
from utils import relative


def getSearchKeywordsRecommendation(keywords, encoding="JSON"):
    root = etree.Element("getSearchKeywordsRecommendation", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords
    
    request = etree.tostring(root, pretty_print=True)
    return get_response(getSearchKeywordsRecommendation.__name__, request, encoding)
    
def findItemsByKeywords(encoding="JSON"):
    root = etree.Element("findItemsByKeywords", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByKeywords.__name__, request, encoding)
    
def findItemsByCategory(encoding="JSON"):
    root = etree.Element("findItemsByCategory", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByCategory.__name__, request, encoding)
    
def findItemsAdvanced(encoding="JSON"):
    root = etree.Element("findItemsAdvanced", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsAdvanced.__name__, request, encoding)
    
def findItemsByProduct(encoding="JSON"):
    root = etree.Element("findItemsByProduct", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByProduct.__name__, request, encoding)
    
def findItemsIneBayStores(encoding="JSON"):
    root = etree.Element("findItemsIneBayStores", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsIneBayStores.__name__, request, encoding)
    
def getHistograms(encoding="JSON"):
    root = etree.Element("getHistograms", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    request = etree.tostring(root, pretty_print=True)
    return get_response(getHistograms.__name__, request, encoding)

def get_response(operation_name, data, encoding, http_headers_dict={}):
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", "finding")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-APPNAME": app_name,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(http_headers_dict)
    
    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
