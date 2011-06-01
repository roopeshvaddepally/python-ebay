from ConfigParser import ConfigParser
from pprint import pprint

import requests
from utils import relative


def getSearchKeywordsRecommendation(keywords):
    if not keywords: print "enter a keyword"
    response = get_response({
            "OPERATION-NAME": getSearchKeywordsRecommendation.__name__, 
            "keywords":keywords
            })
    return response
    
def findItemsByKeywords(): pass
def findItemsByCategory(categoryId, afflite=[], buyerPostalCode=None, 
                        paginationInput=[], sortOrder=None, 
                        aspectFilter=None, domainFilter=None, 
                        itemFilter=None, outputSelector=None): 
    if not categoryId: print "enter a category id"
    response = get_response({
            "OPERATION-NAME": findItemsByCategory.__name__,
            "categoryId": categoryId,
            })
    return response

def findItemsAdvanced(): pass
def findItemsByProduct(): pass
def findItemsIneBayStores(): pass
def getHistograms(): pass

def get_response(params={}):
    endpoint = "http://svcs.sandbox.ebay.com"
    url = "/services/search/FindingService/v1"
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    app_name = config.get("keys", "app_name")
    p = {
        "SERVICE-VERSION": "1.9.0",
        "SECURITY-APPNAME": app_name,
        "RESPONSE-DATA-FORMAT": "JSON",
    }
    p.update(params)
    pprint(p)
    response = requests.get(endpoint+url, params=p)
    pprint(response.url)
    return response.content
