import urllib2
from lxml import etree

from ConfigParser import ConfigParser
from utils import relative


def getSearchKeywordsRecommendation(keywords, encoding="JSON", global_id="EBAY-US"):
    root = etree.Element("getSearchKeywordsRecommendation", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    request = etree.tostring(root, pretty_print=True)
    return get_response(getSearchKeywordsRecommendation.__name__, request, encoding, global_id)


def findItemsByKeywords(keywords, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        paginationInput=None, \
                        sortOrder=None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON", \
                        global_id="EBAY-US"):
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
        sortOrder_elemtext = sortOrder

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
            outputSelector_elemtext = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByKeywords.__name__, request, encoding, global_id)


def findItemsByCategory(categoryId, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        sortOrder=None, \
                        paginationInput = None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON", \
                        global_id="EBAY-US"):
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
        sortOrder_elemtext = sortOrder

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
            outputSelector_elemtext = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByCategory.__name__, request, encoding, global_id)


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
                      encoding="JSON", \
                      global_id="EBAY-US"):
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
        sortOrder_elemtext = sortOrder

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
            outputSelector_elemtext = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsAdvanced.__name__, request, encoding, global_id)


def findItemsByProduct(keywords=None, \
                       productId=None, \
                       affiliate=None, \
                       buyerPostalCode=None, \
                       paginationInput=None, \
                       sortOrder=None, \
                       itemFilter=None, \
                       outputSelector=None, \
                       encoding="JSON", \
                       global_id="EBAY-US"):
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
        sortOrder_elemtext = sortOrder

    #outputSelector is a list
    if outputSelector:
        for item in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elemtext = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsByProduct.__name__, request, encoding, global_id)


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
                          encoding="JSON", \
                          global_id="EBAY-US"):
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
        sortOrder_elemtext = sortOrder

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
            outputSelector_elemtext = item

    request = etree.tostring(root, pretty_print=True)
    return get_response(findItemsIneBayStores.__name__, request, encoding, global_id)


def getHistograms(categoryId, encoding="JSON", global_id="EBAY-US"):
    root = etree.Element("getHistograms", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    categoryId_elem = etree.SubElement(root, "categoryId")
    categoryId_elem.text = categoryId

    request = etree.tostring(root, pretty_print=True)
    return get_response(getHistograms.__name__, request, encoding, global_id)


def get_response(operation_name, data, encoding, global_id, **headers):
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", "finding")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-APPNAME": app_name,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding,
                    "X-EBAY-SOA-GLOBAL-ID": global_id
    }

    http_headers.update(headers)

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
