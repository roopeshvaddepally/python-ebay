import requests

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request


# Item Search
def FindProducts(query, available_items, max_entries, encoding="JSON"):
    
    user_param={'callname' : FindProducts.__name__,
                'responseencoding' : encoding,
                 'QueryKeywords' : query,
                 'AvailableItemsOnly' : available_items,
                 'MaxEntries' : max_entries}
    
    response = get_response(user_param)
    return response.content
    
def FindHalfProducts(query=None, max_entries=None, product_type=None, product_value=None, include_selector=None, encoding="JSON"):                  
    if product_type and product_value and include_selector:
        user_param = {'callname' : FindHalfProducts.__name__,
                      'responseencoding' : encoding, 
                      'ProductId.type' : product_type,
                      'ProductId.Value' : product_value,
                      'IncludeSelector' : include_selector}
        
    if query and max_entries:
        user_param = {'callname' : FindHalfProducts.__name__,
                  'responseencoding' : encoding,
                  'QueryKeywords' : query,
                  'MaxEntries' : max_entries}

    response = get_response(user_param)
    return response.content

# Item Data
def GetSingleItem(item_id, include_selector=None, encoding="JSON"):
    user_param={'callname' : GetSingleItem.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    if include_selector:
        user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content
    
def GetItemStatus(item_id, encoding="JSON"):
    user_param={'callname' : GetItemStatus.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    response = get_response(user_param)
    return response.content
    
def GetShippingCosts(item_id, destination_country_code, destination_postal_code, details, quantity_sold, encoding="JSON"):
    user_param={'callname' : GetShippingCosts.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id,
                'DestinationCountryCode' : destination_country_code, 
                'DestinationPostalCode' : destination_postal_code, 
                'IncludeDetails' : details, 
                'QuantitySold' : quantity_sold}
    
    response = get_response(user_param)
    return response.content 
    
def GetMultipleItems(item_id, include_selector=None, encoding="JSON"):
    user_param={'callname' : GetMultipleItems.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}
    
    if include_selector:
        user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content

# User Reputation
def GetUserProfile(user_id, include_selector=None, encoding="JSON"):
    user_param={'callname' : GetUserProfile.__name__,
                'responseencoding' : encoding,
                'UserID' : user_id}
   
    if include_selector:
       user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content
 

# eBay pop!
def FindPopularSearches(query, category_id=None, encoding="JSON"):
    user_param={'callname' : FindPopularSearches.__name__,
                'responseencoding' : encoding,
                'QueryKeywords' : query}
   
    if category_id:
       user_param['CategoryID'] = category_id
    
    response = get_response(user_param)
    return response.content

    
def FindPopularItems(query, category_id_exclude=None, encoding="JSON"):
    user_param={'callname' : FindPopularItems.__name__,
                'responseencoding' : encoding,
                'QueryKeywords' : query}
   
    if category_id_exclude:
       user_param['CategoryIDExclude'] = category_id_exclude
    
    response = get_response(user_param)
    return response.content

    
# Search: Bug in eBay documentation of Product Id: http://developer.ebay.com/devzone/shopping/docs/callref/FindReviewsAndGuides.html#Samples
def FindReviewsandGuides(category_id=None, product_id=None, encoding="JSON"):
    if category_id:
        user_param={'callname' : FindReviewsandGuides.__name__,
                'responseencoding' : encoding,
                'CategoryID' : category_id}
   
    if product_id:
        user_param={'callname' : FindReviewsandGuides.__name__,
                'responseencoding' : encoding,
                'ProductID' : product_id}
                
    response = get_response(user_param)
    return response.content


# Utilities
def GetCategoryInfo(category_id, include_selector=None, encoding="JSON"):
    if category_id:
        user_param={'callname' : GetCategoryInfo.__name__,
                'responseencoding' : encoding,
                'CategoryID' : category_id}
   
    if include_selector:
        user_param['IncludeSelector'] = include_selector 
                
    response = get_response(user_param)
    return response.content
 
def GeteBayTime(encoding="JSON"):
    user_param={'callname' : GeteBayTime.__name__,
                'responseencoding' : encoding}
                
    response = get_response(user_param)
    return response.content 
    

#requests method
def get_response(user_params):
    config = get_config_store()
    app_id = config.get("keys", "app_name")
    site_id = config.get("call", "siteid")
    version = config.get("call", "compatibility_level")
    endpoint = config.get("endpoints", "shopping")

    d=dict(appid = app_id, siteid = site_id, version = version)
    
    d.update(user_params)
    
    return requests.get(endpoint, params=d)
