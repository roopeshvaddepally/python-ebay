# import urllib2

from lxml import etree

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request


def getDeals(keywords, encoding="JSON"):
    #not documented in ebay docs. Need to raise a ticket
    root = etree.Element("getDealsRequest", xmlns="http://www.ebay.com/marketplace/services")

    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    request = etree.tostring(root, pretty_print=True)
    return get_response(getDeals.__name__, request, encoding)


def getMostWatchedItems(affiliate=None, maxResults=None,categoryId=None, encoding="JSON"):
    root = etree.Element("getMostWatchedItemsRequest", xmlns="http://www.ebay.com/marketplace/services")

    #affiliate is dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate.keys():
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if maxResults:
        maxResults_elem = etree.SubElement(root, "maxResults")
        maxResults_elem.text = maxResults

    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId


    request = etree.tostring(root, pretty_print=True)
    return get_response(getMostWatchedItems.__name__, request, encoding)


#Takes categoryId or itemId
def getRelatedCategoryItems(affiliate=None, \
                            maxResults=None, \
                            categoryId=None, \
                            itemFilter=None, \
                            itemId=None, \
                            encoding="JSON"):
    root = etree.Element("getRelatedCategoryItemsRequest", xmlns="http://www.ebay.com/marketplace/services")

    #affiliate is dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate.keys():
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if maxResults:
        maxResults_elem = etree.SubElement(root, "maxResults")
        maxResults_elem.text = maxResults

    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId

    #itemFilter is list of dicts
    if itemFilter and len(itemFilter)>0:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in itemFilter.keys():
                itemId_elem = etree.SubElement(itemFilter_elem, key)
                itemId_elem.text =  itemFilter[key]

    if itemId:
        itemId_elem = etree.SubElement(root, "itemId")
        itemId_elem.text = itemId

    request = etree.tostring(root, pretty_print=True)
    return get_response(getRelatedCategoryItems.__name__, request, encoding)


def getSimilarItems(affiliate=None, \
                    maxResults=None, \
                    categoryId=None, \
                    categoryIdExclude=None, \
                    endTimeFrom=None, \
                    endTimeTo=None, \
                    itemFilter=None, \
                    itemId=None, \
                    listingType=None, \
                    maxPrice=None, \
                    encoding="JSON"):
    root = etree.Element("getSimilarItemsRequest", xmlns="http://www.ebay.com/marketplace/services")

    #affiliate is dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate.keys():
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if maxResults:
        maxResults_elem = etree.SubElement(root, "maxResults")
        maxResults_elem.text = maxResults

    #categoryId is list
    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId

    #categoryIdExclude is list
    if categoryIdExclude:
        for cat_id in categoryIdExclude:
           categoryIdExclude_elem = etree.SubElement(root, "categoryIdExclude")
           categoryIdExclude_elem.text = cat_id

    if endTimeFrom and endTimeTo:
        endTimeFrom_elem = etree.SubElement(root, "endTimeFrom")
        endTimeFrom_elem = endTimeFrom
        endTimeTo_elem = etree.SubeElement(root, "endTimeTo")
        endTimeTo_elem = endTimeTo

    #itemFilter is list of dicts
    if itemFilter and len(itemFilter)>0:
        for item in itemFilter:
            itemFilter_elem = etree.SubElement(root, "itemFilter")
            for key in itemFilter.keys():
                itemId_elem = etree.SubElement(itemFilter_elem, key)
                itemId_elem.text =  itemFilter[key]

    if itemId:
        itemId_elem = etree.SubElement(root, "itemId")
        itemId_elem.text = itemId

    if listingType:
        listingType_elem = etree.SubElement(root, "listingType")
        listingType_elem.text = listingType

    if maxPrice:
        maxPrice_elem = etree.SubElement(root, "maxPrice")
        maxPrice_elem.text = maxPrice


    request = etree.tostring(root, pretty_print=True)
    return get_response(getSimilarItems.__name__, request, encoding)


def getTopSellingProducts(affiliate=None, maxResults=None, encoding="JSON"):
    root = etree.Element("getTopSellingProductsRequest", xmlns="http://www.ebay.com/marketplace/services")

    #affiliate is dict
    if affiliate:
        affiliate_elem = etree.SubElement(root, "affiliate")
        for key in affiliate.keys():
            key_elem = etree.SubElement(affiliate_elem, key)
            key_elem.text = affiliate[key]

    if maxResults:
        maxResults_elem = etree.SubElement(root, "maxResults")
        maxResults_elem.text = maxResults


    request = etree.tostring(root, pretty_print=True)
    return get_response(getTopSellingProducts.__name__, request, encoding)


def get_response(operation_name, data, encoding, **headers):
    config = get_config_store()
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", "merchandising")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "EBAY-SOA-CONSUMER-ID": app_name,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    return data

