# import urllib2

from lxml import etree

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request
    
def findBestMatchItemDetailsAcrossStores(keywords, \
                                         siteResultsPerPage, \
                                         categoryId=None, \
                                         entriesPerPage=None, \
                                         ignoreFeatured=None, \
                                         itemFilter=None, \
                                         outputSelector=None, \
                                         postSearchItemFilter=None, \
                                         postSearchSellerFilter=None, \
                                         encoding="JSON"):
    root = etree.Element("findBestMatchItemDetailsAcrossStoresRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    root = get_generic_tags(root=root, \
                            keywords=keywords, \
                            siteResultsPerPage=siteResultsPerPage, \
                            categoryId=categoryId, \
                            entriesPerPage=entriesPerPage, \
                            ignoreFeatured=ignoreFeatured, \
                            itemFilter=itemFilter, \
                            outputSelector=outputSelector, \
                            postSearchItemFilter=postSearchItemFilter, \
                            postSearchSellerFilter=postSearchSellerFilter)

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsAcrossStores.__name__, request, encoding)



def findBestMatchItemDetailsAdvanced(keywords, \
                                     siteResultsPerPage, \
                                     categoryId=None, \
                                     entriesPerPage=None, \
                                     ignoreFeatured=None, \
                                     itemFilter=None, \
                                     outputSelector=None, \
                                     postSearchItemFilter=None, \
                                     postSearchSellerFilter=None, \
                                     encoding="JSON"):
    root = etree.Element("findBestMatchItemDetailsAdvancedRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    root = get_generic_tags(root=root, \
                            keywords=keywords, \
                            siteResultsPerPage=siteResultsPerPage, \
                            categoryId=categoryId, \
                            entriesPerPage=entriesPerPage, \
                            ignoreFeatured=ignoreFeatured, \
                            itemFilter=itemFilter, \
                            outputSelector=outputSelector, \
                            postSearchItemFilter=postSearchItemFilter, \
                            postSearchSellerFilter=postSearchSellerFilter)

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsAdvanced.__name__, request, encoding)



def findBestMatchItemDetailsByCategory(categoryId, \
                                       siteResultsPerPage, \
                                       entriesPerPage=None, \
                                       ignoreFeatured=None, \
                                       itemFilter=None, \
                                       outputSelector=None, \
                                       postSearchItemFilter=None, \
                                       postSearchSellerFilter=None, \
                                       encoding="JSON"):
    root = etree.Element("findBestMatchItemDetailsByCategoryRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    root = get_generic_tags(root=root, \
                            categoryId=categoryId, \
                            siteResultsPerPage=siteResultsPerPage, \
                            entriesPerPage=entriesPerPage, \
                            ignoreFeatured=ignoreFeatured, \
                            itemFilter=itemFilter, \
                            outputSelector=outputSelector, \
                            postSearchItemFilter=postSearchItemFilter, \
                            postSearchSellerFilter=postSearchSellerFilter)

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsByCategory.__name__, request, encoding)



def findBestMatchItemDetailsByKeywords(keywords, \
                                       siteResultsPerPage, \
                                       entriesPerPage=None, \
                                       ignoreFeatured=None, \
                                       itemFilter=None, \
                                       outputSelector=None, \
                                       postSearchItemFilter=None, \
                                       postSearchSellerFilter=None, \
                                       encoding="JSON"):
    root = etree.Element("root", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    root = get_generic_tags(root=root, \
                            keywords=keywords, \
                            siteResultsPerPage=siteResultsPerPage, \
                            entriesPerPage=entriesPerPage, \
                            ignoreFeatured=ignoreFeatured, \
                            itemFilter=itemFilter, \
                            outputSelector=outputSelector, \
                            postSearchItemFilter=postSearchItemFilter, \
                            postSearchSellerFilter=postSearchItemFilter)

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsByKeywords.__name__, request, encoding)



def findBestMatchItemDetailsByProduct(productId, \
                                      siteResultsPerPage, \
                                      entriesPerPage=None, \
                                      ignoreFeatured=None, \
                                      itemFilter=None, \
                                      outputSelector=None, \
                                      postSearchItemFilter=None, \
                                      postSearchSellerFilter=None, \
                                      encoding="JSON"):
    root = etree.Element("findBestMatchItemDetailsByProductRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    root = get_generic_tags(root=root, \
                            productId=productId, \
                            siteResultsPerPage=siteResultsPerPage, \
                            entriesPerPage=entriesPerPage, \
                            ignoreFeatured=ignoreFeatured, \
                            itemFilter=itemFilter, \
                            outputSelector=outputSelector, \
                            postSearchItemFilter=postSearchItemFilter, \
                            postSearchSellerFilter=postSearchItemFilter)

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsByProduct.__name__, request, encoding)



def findBestMatchItemDetailsBySeller(categoryId, \
                                     sellerUserName, \
                                     ignoreFeatured=None, \
                                     itemFilter=None, \
                                     paginationInput=None, \
                                     encoding="JSON"):
    root = etree.Element("findBestMatchItemDetailsBySellerRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")

    categoryId_elem = etree.SubElement(root, "categoryId")
    categoryId_elem.text = categoryId

    sellerUserName_elem = etree.SubElement(root, "sellerUserName")
    sellerUserName_elem.text = sellerUserName

    if ignoreFeatured:
        ignoreFeatured_elem = etree.SubElement(root, "ignoreFeatured")
        ignoreFeatured_elem.text = ignoreFeatured

    #itemFilter is a List of dicts: [{"paramName" : "PriceMin", "paramValue" : "50", "name" : "Currency", "value" : "USD"}]

    if itemFilter:
        for item_filter in itemFilter:
            if len(item_filter)>0:
                itemFilter_elem = etree.SubElement(root, "itemFilter")
                for key in item_filter.keys():
                    item_elem = etree.SubElement(itemFilter_elem, key)
                    item_elem.text = item_filter[key]

    # paginationInput is a dict: {entriesPerPage:5, pageNumber:10}
    if paginationInput and len(paginationInput)>0:
        paginationInput_elem = etree.SubElement(root, "paginationInput")
        for key in paginationInput.keys():
            input_values_elem = etree.SubElement(paginationInput_elem, key)
            input_values_elem.text = paginationInput[key]

    request = etree.tostring(root, pretty_print=True)
    return get_response(findBestMatchItemDetailsBySeller.__name__, request, encoding)


#Not working
def findBestMatchItemDetails(encoding="JSON"):
    request = """<?xml version="1.0" encoding="utf-8"?>
<getBestMatchItemDetailsRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <itemId>13474073440</itemId>
  <itemId>23484479761</itemId>
</getBestMatchItemDetailsRequest>"""

    return get_response(findBestMatchItemDetails.__name__,request, encoding)

def getVersion():
    root = etree.Element("getVersionRequest", xmlns="http://www.ebay.com/marketplace/search/v1/services")
    request=etree.tostring(root, pretty_print=True)

    return get_response(getVersion.__name__, request, encoding="JSON")

def get_generic_tags(root, siteResultsPerPage, productId=None, keywords=None, categoryId=None, entriesPerPage=None, ignoreFeatured=None, itemFilter=None, outputSelector=None, postSearchItemFilter=None, postSearchSellerFilter=None):

    siteResultsPerPage_elem = etree.SubElement(root, "siteResultsPerPage")
    siteResultsPerPage_elem.text = siteResultsPerPage

    if keywords:
        keywords_elem = etree.SubElement(root, "keywords")
        keywords_elem.text = keywords

    if entriesPerPage:
        entriesPerPage_elem = etree.SubElement(root, "entriesPerPage")
        entriesPerPage_elem.text = entriesPerPage

    if ignoreFeatured:
        ignoreFeatured_elem = etree.SubElement(root, "ignoreFeatured")
        ignoreFeatured_elem.text = ignoreFeatured

    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId

    if productId:
        productId_elem = etree.SubElement(root, "productId")
        productId_elem.text = productId

    #itemFilter is a List of dicts: [{paramName=PriceMin, paramValue=50, name=Currency, value=USD}]
    if itemFilter:
        for item_filter in itemFilter:
            if len(item_filter)>0:
                itemFilter_elem = etree.SubElement(root, "itemFilter")
                for key in item_filter.keys():
                    item_elem = etree.SubElement(itemFilter_elem, key)
                    item_elem.text = item_filter[key]

    #outputSelector is a List
    if outputSelector and len(outputSelector)>0:
        for output_selector in outputSelector:
            outputSelector_elem = etree.SubElement(root, "outputSelector")
            outputSelector_elem.text = output_selector


    # postSearchItemFilter is a List
    if postSearchItemFilter and len(postSearchItemFilter)>0:
        postSearchItemFilter_elem = etree.SubElement(root, "postSearchItemFilter")
        for item_filter in postSearchItemFilter:
            itemId_elem = etree.SubElement(postSearchItemFilter_elem, "itemId")
            itemId_elem.text = item_filter

    # postSearchSellerFilter is a List
    if postSearchSellerFilter and len(postSearchSellerFilter)>0:
        postSearchSellerFilter_elem = etree.SubElement(root, "postSearchSellerFilter")
        for seller in postSearchSellerFilter:
            seller_elem = etree.SubElement(postSearchSellerFilter_elem, "sellerUserName")
            seller_elem.text = seller

    return root


def get_response(operation_name, data, encoding, **headers):
    config = get_config_store()
    access_token = config.get("auth", "token")
    endpoint = config.get("endpoints", "best_match")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-TOKEN": access_token,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    return data
