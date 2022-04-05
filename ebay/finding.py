from lxml import etree

# import urllib2

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request

def getSearchKeywordsRecommendation( keywords, encoding="JSON", **headers ):
    root = etree.Element("getSearchKeywordsRecommendation",
            xmlns="http://www.ebay.com/marketplace/search/v1/services")
    keywords_elem = etree.SubElement(root, "keywords")
    keywords_elem.text = keywords

    request = etree.tostring(root, pretty_print=True)
    return get_response(
        getSearchKeywordsRecommendation.__name__, request, encoding,
        **headers )


def findItemsByKeywords(keywords, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        paginationInput=None, \
                        sortOrder=None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON",
                        **headers ):
    root = etree.Element("findItemsByKeywords",
                    xmlns="http://www.ebay.com/marketplace/search/v1/services")

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
    return get_response(findItemsByKeywords.__name__, request, encoding,
                        **headers )


def findItemsByCategory(categoryId, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        sortOrder=None, \
                        paginationInput = None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON",
                        **headers ):
    root = etree.Element("findItemsByCategory",
                    xmlns="http://www.ebay.com/marketplace/search/v1/services")

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
    return get_response(findItemsByCategory.__name__, request, encoding,
                        **headers )


def findItemsAdvanced(  keywords=None, \
                        categoryId=None, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        paginationInput = None, \
                        sortOrder=None, \
                        aspectFilter=None, \
                        domainFilter=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON",
                        **headers ):
    root = etree.Element("findItemsAdvanced",
                    xmlns="http://www.ebay.com/marketplace/search/v1/services")

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
    return get_response(findItemsAdvanced.__name__, request, encoding,
                        **headers )


def findItemsByProduct( keywords=None, \
                        productId=None, \
                        affiliate=None, \
                        buyerPostalCode=None, \
                        paginationInput=None, \
                        sortOrder=None, \
                        itemFilter=None, \
                        outputSelector=None, \
                        encoding="JSON",
                        **headers ):
    root = etree.Element("findItemsByProduct",
                         xmlns="http://www.ebay.com/marketplace/search/v1/services")

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
    return get_response(findItemsByProduct.__name__, request, encoding,
                        **headers )


def findItemsIneBayStores(  keywords=None, \
                            storeName=None, \
                            affiliate=None, \
                            buyerPostalCode=None, \
                            paginationInput=None, \
                            sortOrder=None, \
                            aspectFilter=None, \
                            domainFilter=None, \
                            itemFilter=None, \
                            outputSelector=None, \
                            encoding="JSON",
                            **headers ):
    root = etree.Element("findItemsIneBayStores",
                    xmlns="http://www.ebay.com/marketplace/search/v1/services")

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
    return get_response(findItemsIneBayStores.__name__, request, encoding,
                        **headers )


def getHistograms(categoryId, encoding="JSON"):
    root = etree.Element("getHistograms",
                    xmlns="http://www.ebay.com/marketplace/search/v1/services")

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

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    #
    return data
