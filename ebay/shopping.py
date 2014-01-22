"""
Implementation of eBay's "Shopping API".
    
TODO: Implement all arguments. Many functions implement only a subset of the 
      arguments that are available in the eBay API call.
          
http://developer.ebay.com/Devzone/shopping/docs/CallRef/index.html
"""

import requests
from utils import get_config_store


# Item Search
def FindProducts(query, available_items, max_entries, encoding="JSON"):
    """
    Return well known information about products (not actual items).
    Especially return the ``ProductID`` of a certain product.
    
    To search for items look at the finding API.
    
    TODO: Implement all arguments. Depending on its arguments, this API call 
          can also return items.
    
    http://developer.ebay.com/Devzone/shopping/docs/CallRef/FindProducts.html
    """
    user_param={'callname' : FindProducts.__name__,
                'responseencoding' : encoding,
                 'QueryKeywords' : query,
                 'AvailableItemsOnly' : available_items,
                 'MaxEntries' : max_entries}
    
    response = get_response(user_param)
    return response.content
    
def FindHalfProducts(query=None, max_entries=None, product_type=None, 
                     product_value=None, include_selector=None, 
                     encoding="JSON"):
    """
    Search ``half.com`` for information about products (not actual items).
    
    TODO: Calling this function with default arguments results in error.
    
    http://developer.ebay.com/DevZone/shopping/docs/CallRef/FindHalfProducts.html
    """
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
    """
    Return information about a single item (listing) that can be bought.
        
    Parameters
    ----------
    
    item_id: str
        Id of an item. Item IDs can be obtained with the Finding API.
    
    include_selector: str, None
        Specify the amount of information that is returned. 
        If ``None`` a small number of default fields is returned.
        Can consist of multiple words separated by commas. Possible values:
        
        Details, Description, TextDescription, ShippingCosts, ItemSpecifics,
        Variations, Compatibility

    encoding: str
        Format of the returned data, possible values: "JSON", "XML"

    See also
    --------
    
    http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetSingleItem.html
    """
    user_param={'callname' : GetSingleItem.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    if include_selector:
        user_param['IncludeSelector'] = include_selector
    
    response = get_response(user_param)
    return response.content
    
def GetItemStatus(item_id, encoding="JSON"):
    """
    Return information that frequently changes (for example: current price),
    on an item.
    
    TODO: Make this call work with multiple item ids.
        
    developer.ebay.com/DevZone/shopping/docs/CallRef/GetItemStatus.html
    """
    user_param={'callname' : GetItemStatus.__name__,
                'responseencoding' : encoding,
                'ItemId' : item_id}

    response = get_response(user_param)
    return response.content
    
def GetShippingCosts(item_id, destination_country_code, destination_postal_code, 
                     details, quantity_sold, encoding="JSON"):
    """
    Return the shipping costs for an item.
    
    Parameters
    ----------
    
    destination_country_code: str
        Code that identifies the destination country. 
        For example: USA: "US", Germany: "DE"
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/types/CountryCodeType.html

    destination_postal_code: str
        Postal code of the destination, country specific. 
        For example: "52068": eastern Aachen, Germany; 
        "10027": central New York City, USA
    
    details: bool
        If true: return more detailed information.
        
    quantity_sold: int
        Number of items that should be shipped together.
        
    encoding: str
        Format of the returned data, possible values "JSON", "XML"

    See also
    --------
    
    http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetShippingCosts.html
    """
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
    """
    Return details about multiple items (listings) on eBay.
    
    Parameters
    ----------
    
    item_id: str
        Id of one item, or comma separated list of item IDs (without any 
        space characters). Item IDs can be obtained with the Finding API.
    
    include_selector: str, None
        Specify the amount of information that is returned. 
        If ``None`` a small number of default fields is returned.
        Can consist of multiple words separated by commas. Possible values:
        
        Details, Description, TextDescription, ShippingCosts, ItemSpecifics,
        Variations, Compatibility

    encoding: str
        Format of the returned data, possible values: "JSON", "XML"

    See also
    --------
    
    http://developer.ebay.com/Devzone/shopping/docs/CallRef/GetMultipleItems.html
    """
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
