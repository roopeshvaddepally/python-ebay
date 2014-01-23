"""
Implementation of eBay's "Finding API".
 
http://developer.ebay.com/DevZone/finding/CallRef/index.html
"""

import urllib2
from lxml import etree

from utils import get_config_store


def getSearchKeywordsRecommendation(keywords, encoding="JSON"):
    root = etree.Element("getSearchKeywordsRecommendation", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    request = etree.tostring(root, pretty_print=True)
    return get_response(getSearchKeywordsRecommendation.__name__, request, encoding)


def findItemsByKeywords(keywords, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        paginationInput=None, \
                        sortOrder=None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON"):
    """
    Search for items by keywords. 
    
    This call returns only little information about each item. However it
    returns item IDs, that uniquely identify each item that is sold on eBay. 
    
    Detailed information about items can be obtained with the functions
    ``ebay.shopping.GetMultipleItems`` and ``ebay.shopping.GetSingleItem``.
    These functions need item IDs as their input values.
       
    Parameters
    ----------
    
    keywords: str
        Keywords for the search.
    
    affiliate: dict, None
        Information that enable affiliates to receive their commission.
        This information does not affect the search itself. For details
        on the content of the dictionary see:
        
        http://developer.ebay.com/DevZone/finding/CallRef/types/Affiliate.html
        
        Example::
        
            affiliate = {"networkId":"9", "trackingId":"1234567890"}

    buyerPostalCode: str, None
        The postal code of the buyer. Used to limit distance between buyer
        and seller.

    paginationInput: dict, None
        Control the number of returned items per call. Also used to access
        the next page (or lot) of returned items.
        
        The maximum number of items per call is 100, the maximum number of 
        pages is 100. Therefore the maximum number of results per search 
        is 10000.
        
        Example with 10 items per call, to access page 3 of the search 
        results::
        
            paginationInput = {"entriesPerPage": "10", "pageNumber": "3"}
        
    sortOrder: str, None
        The sort order of the results. Possible values:
        
        None, "EndTimeSoonest", "BestMatch", 
        "BidCountFewest", "BidCountMost", "CountryAscending", 
        "CountryDescending", "CurrentPriceHighest", "DistanceNearest", 
        "PricePlusShippingHighest", "PricePlusShippingLowest", "StartTimeNewest"

    aspectFilter: list of dict, None
        Limit the results items with certain properties. These properties
        are (physical) properties of the items themselves.
        
        The dictionaries have two keys:
        * ``aspectName``: Name of a property, for example "Color".
        * ``aspectValueName``: Value of that property, for example "Black". 
    
        Example::
        
            aspectFilter =  [{"aspectName":"Color", "aspectValueName":"Black"}, 
                             {"aspectName":"", "aspectValueName":""}]

    domainFilter: list of dicts, None
        Limit the results to a certain product domain.
    
        Only a single dictionary can sensibly be put into the list,
        because multiple domain filters are currently unsupported.
        
        The dictionary has only one key: 
        * "domainName": The name of the desired product domain.
        
        Example::
        
            domainFilter = [{"domainName": "Other_MP3_Players"}] 

    itemFilter: list of dicts, None
        Limit the results to items with certain properties. These properties
        are properties of the auction. 
        
        The dictionaries can have various keys. Please consult eBay's 
        documentation for details: 
        http://developer.ebay.com/DevZone/finding/CallRef/types/ItemFilterType.html

        Example that sets a minimum and maximum price in Euro::
        
            itemFilter = [{"name":"MaxPrice", "value":"100", 
                           "paramName":"Currency", "paramValue":"EUR"}, 
                          {"name":"MinPrice", "value":"50", 
                           "paramName":"Currency", "paramValue":"EUR"}]
        
    outputSelector: list of str, None
        Control the amount and type of information that is returned.
    
        Possible values are:
        "AspectHistogram", "CategoryHistogram", "ConditionHistogram", 
        "GalleryInfo", "PictureURLLarge", "PictureURLSuperSize", "SellerInfo", 
        "StoreInfo", "UnitPriceInfo"
        
        Example::
        
            outputSelector = ["StoreInfo", "SellerInfo", "AspectHistogram"]

    encoding: str
        Format of the returned data, possible values: "JSON", "XML"

    See also
    --------
    
    http://developer.ebay.com/DevZone/finding/CallRef/findItemsByKeywords.html
    """
    root = etree.Element("findItemsByKeywords", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    #affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    #paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    #itemFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    #sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    #aspectFilter is a list of dicts
    if aspectFilter:
        for item in aspectFilter:
            aspectFilter_elem = etree.SubElement(root, "aspectFilter")
            for key in item:
                key_elem = etree.SubElement(aspectFilter_elem, key)
                key_elem.text = item[key]

    #domainFilter is a list of dicts
    if domainFilter:
        for item in domainFilter:
            domainFilter_elem = etree.SubElement(root, "domainFilter")
            for key in item:
                key_elem = etree.SubElement(domainFilter_elem, key)
                key_elem.text = item[key]

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByKeywords.__name__, request, encoding)


def findItemsByCategory(categoryId, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        sortOrder=None, \
                        paginationInput = None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON"):
    root = etree.Element("findItemsByCategory", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    categoryId_elem = etree.SubElement(root, "categoryId")
    categoryId_elem.text = categoryId

    #affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    #paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    #itenFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    #sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    #aspectFilter is a list of dicts
    if aspectFilter:
        for item in aspectFilter:
            aspectFilter_elem = etree.SubElement(root, "aspectFilter")
            for key in item:
                key_elem = etree.SubElement(aspectFilter_elem, key)
                key_elem.text = item[key]

    #domainFilter is a list of dicts
    if domainFilter:
        for item in domainFilter:
            domainFilter_elem = etree.SubElement(root, "domainFilter")
            for key in item:
                key_elem = etree.SubElement(domainFilter_elem, key)
                key_elem.text = item[key]

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByCategory.__name__, request, encoding)


def findItemsAdvanced(keywords=None, \
                      categoryId=None, \
                      affiliate=None, \
                      buyerPostalCode=None, \
                      paginationInput = None, \
                      sortOrder=None, \
                      aspectFilter=None, \
                      domainFilter=None, \
                      itemFilter=None, \
                      outputSelector=None, \
                      encoding="JSON"):
    root = etree.Element("findItemsAdvanced", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    if keywords:
        keywords_elem = etree.SubElement(root, "keywords")
        keywords_elem.text = keywords

    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId

    #affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    #paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    #itenFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    #sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    #aspectFilter is a list of dicts
    if aspectFilter:
        for item in aspectFilter:
            aspectFilter_elem = etree.SubElement(root, "aspectFilter")
            for key in item:
                key_elem = etree.SubElement(aspectFilter_elem, key)
                key_elem.text = item[key]

    #domainFilter is a list of dicts
    if domainFilter:
        for item in domainFilter:
            domainFilter_elem = etree.SubElement(root, "domainFilter")
            for key in item:
                key_elem = etree.SubElement(domainFilter_elem, key)
                key_elem.text = item[key]

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsAdvanced.__name__, request, encoding)


def findItemsByProduct(keywords=None, \
                       productId=None, \
                       affiliate=None, \
                       buyerPostalCode=None, \
                       paginationInput=None, \
                       sortOrder=None, \
                       itemFilter=None, \
                       outputSelector=None, \
                       encoding="JSON"):
    root = etree.Element("findItemsByProduct", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    if keywords:
        keywords_elem = etree.SubElement(root, "keywords")
        keywords_elem.text = keywords

    if productId:
        productId_elem = etree.SubElement(root, "productId", type="string")
        productId_elem.text = productId

    #affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    #paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    #itenFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    #sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByProduct.__name__, request, encoding)


def findItemsIneBayStores(keywords=None, \
                          storeName=None, \
                          affiliate=None, \
                          buyerPostalCode=None, \
                          paginationInput=None, \
                          sortOrder=None, \
                          aspectFilter=None, \
                          domainFilter=None, \
                          itemFilter=None, \
                          outputSelector=None, \
                          encoding="JSON"):
    root = etree.Element("findItemsIneBayStores", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    if keywords:
        keywords_elem = etree.SubElement(root, "keywords")
        keywords_elem.text = keywords

    if storeName:
        storeName_elem = etree.SubElement(root, "storeName")
        storeName_elem.text = storeName

    #affiliate is a dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate:
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if buyerPostalCode:
        buyerPostalCode_elem = etree.SubElement(root, "buyerPostalCode")
        buyerPostalCode_elem.text = buyerPostalCode

    #paginationInput is a dict
    if paginationInput:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput:
            key_elem = etree.SubElement(paginationInput_elem, key)
            key_elem.text = paginationInput[key]

    #itenFilter is a list of dicts
    if itemFilter:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in item:
                key_elem = etree.SubElement(itemFilter_elem, key)
                key_elem.text = item[key]

    #sortOrder
    if sortOrder:
        sortOrder_elem = etree.SubElement(root, "sortOrder")
        sortOrder_elem.text = sortOrder

    #aspectFilter is a list of dicts
    if aspectFilter:
        for item in aspectFilter:
            aspectFilter_elem = etree.SubElement(root, "aspectFilter")
            for key in item:
                key_elem = etree.SubElement(aspectFilter_elem, key)
                key_elem.text = item[key]

    #domainFilter is a list of dicts
    if domainFilter:
        for item in domainFilter:
            domainFilter_elem = etree.SubElement(root, "domainFilter")
            for key in item:
                key_elem = etree.SubElement(domainFilter_elem, key)
                key_elem.text = item[key]

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsIneBayStores.__name__, request, encoding)


def getHistograms(categoryId, encoding="JSON"):
    root = etree.Element("getHistograms", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    categoryId_elem = etree.SubElement(root, "categoryId")
    categoryId_elem.text = categoryId

    request = etree.tostring(root, pretty_print=True)
    return get_response(getHistograms.__name__, request, encoding)


def get_response(operation_name, data, encoding, **headers):
    config = get_config_store()
    globalId = config.get("call", "global_id")
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", "finding")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-APPNAME": app_name,
                    "X-EBAY-SOA-GLOBAL-ID" : globalId,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
