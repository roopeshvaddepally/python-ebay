from ConfigParser import ConfigParser
import requests
from utils import relative

# Item Search
def FindProducts(encoding, query, available_items, max_entries):
    response = get_response(
                    callname= FindProducts.__name__,  
                    responseencoding=encoding,
                    QueryKeywords=query,
                    AvailableItemsOnly=available_items,
                    MaxEntries=max_entries
                    )
    
    return response.content
    
def FindHalfProducts(): pass

# Item Data
def GetSingleItem(): pass
def GetItemStatus(): pass
def GetShippingCosts(): pass
def GetMultipleItems(): pass

# User Reputation
def GetUserProfile(): pass

# eBay pop!
def FindPopularSearches(): pass
def FindPopularItems(): pass

# Search
def FindReviewsandGuides(): pass

# Utilities
def GetCategoryInfo(): pass
def GeteBayTime(): pass 


def get_response(*args, **kwargs):
    endpoint = "http://open.api.sandbox.ebay.com/shopping"
    
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    
    app_id = config.get("keys", "app_name")
    site_id = config.get("call", "siteid")
    version = config.get("call", "compatibility_level")

    d=dict(appid = app_id, siteid = site_id, version = version)
    d.update(kwargs)
    
    return requests.get(endpoint, params=d)
