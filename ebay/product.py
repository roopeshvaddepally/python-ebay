# import urllib2

from lxml import etree
from six import print_ as print3

try:
    from  utils import ( get_config_store, urlopen, Request, Specification,
                         CompatibilityPropertyFilter,  Value, SortOrder )
except ImportError:

def findCompatibilitiesBySpecification(specification, \
                                       categoryId, \
                                       compatibilityPropertyFilter=None, \
                                       dataSet=None, \
                                       datasetPropertyName=None, \
                                       exactMatch=None, \
                                       paginationInput=None, \
                                       sortOrder=None, \
                                       encoding="JSON"):

    root = etree.Element("findCompatibilitiesBySpecificationRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services")

    #specification is an array of objects in Utils.py
    for spec in specification:
        specification_elem = etree.SubElement(root, "specification")
        propertyName_elem = etree.SubElement(specification_elem,"propertyName")
        propertyName_elem.text = spec.propertyName

        for v in spec.values:
            value_elem = etree.SubElement(specification_elem, "value")
            if v.number:
                number_elem = etree.SubElement(value_elem, "number")
                subValue_elem = etree.SubElement(number_elem, "value")
                subValue_elem.text = v.number

            if v.text:
                text_elem = etree.SubElement(value_elem, "text")
                subValue_elem = etree.SubElement(text_elem, "value")
                subValue_elem.text = v.text

            if v.url:
                url_elem = etree.SubElement(value_elem, "URL")
                subValue_elem = etree.SubElement(url_elem, "value")
                subValue_elem.text = v.url

    #compatibilityPropertyFilter is an array of objects in Utils.py
    if compatibilityPropertyFilter:
        for cp_filter in compatibilityPropertyFilter:
            compatibilityPropertyFilter_elem = etree.SubElement(root, "compatibilityPropertyFilter")
            propertyName_elem = etree.SubElement(compatibilityPropertyFilter_elem,"propertyName")
            propertyName_elem.text = cp_filter.propertyName

            for v in cp_filter.values:
                value_elem = etree.SubElement(compatibilityPropertyFilter_elem, "value")
                if v.number:
                    number_elem = etree.SubElement(value_elem, "number")
                    subValue_elem = etree.SubElement(number_elem, "value")
                    subValue_elem.text = v.number

                if v.text:
                    text_elem = etree.SubElement(value_elem, "text")
                    subValue_elem = etree.SubElement(text_elem, "value")
                    subValue_elem.text = v.text

                if v.url:
                    url_elem = etree.SubElement(value_elem, "URL")
                    subValue_elem = etree.SubElement(url_elem, "value")
                    subValue_elem.text = v.url


    categoryId_elem = etree.SubElement(root, "categoryId")
    categoryId_elem.text = categoryId

    #dataSet is a List
    if dataSet:
        for ds in dataSet:
            ds_elem = etree.SubElement(root, "dataSet")
            ds_elem.text = ds

    #datasetPropertyName is a List
    if datasetPropertyName:
        for dpn in datasetPropertyName:
            dpn_elem = etree.SubElement(root, "datasetPropertyName")
            dpn_elem.text = dpn

    if exactMatch:
        exactMatch_elem = etree.SubElement(root, "exactMatch")
        exactMatch_elem.text = exactMatch

    #paginationInput is Dict
    if paginationInput:
        for key in paginationInput.keys():
            key_elem = etree.SubElement(root, key)
            key_elem.text = paginationInput[key]

    #Really weirdly written API by eBay, sortOrder is used two times, confusing naming
    if sortOrder:
        for so in sortOrder:
            sortOrder_elem = etree.SubElement(root, "sortOrder")
            sortPriority_elem = etree.SubElement(sortOrder_elem,"sortPriority")
            sortPriority_elem.text = so.sortPriority

            subSortOrder_elem = etree.SubElement(sortOrder_elem, "sortOrder")
            order_elem = etree.SubElement(subSortOrder_elem, "order")
            order_elem.text = so.order
            propertyName_elem = etree.SubElement(subSortOrder_elem, "propertyName")
            propertyName_elem.text = so.propertyName


    request=etree.tostring(root, pretty_print=True)
    # print request
    print3( request )
    
    return get_response(findCompatibilitiesBySpecification.__name__, request, encoding)


def getProductCompatibilities(datasetPropertyName, \
                              productIdentifier, \
                              applicationPropertyFilter=None, \
                              dataset=None, \
                              disabledProductFilter=None, \
                              paginationInput=None, \
                              sortOrder=None, \
                              encoding="JSON"):
    root = etree.Element("findProductsByCompatibilityRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services")

    #datasetPropertyName is a List
    if datasetPropertyName:
        for dpn in datasetPropertyName:
            dpn_elem = etree.SubElement(root, "datasetPropertyName")
            dpn_elem.text = dpn

    #compatibilityPropertyFilter is an object in Utils.py
    if compatibilityPropertyFilter:
        for cp_filter in compatibilityPropertyFilter:
            compatibilityPropertyFilter_elem = etree.SubElement(root, "compatibilityPropertyFilter")
            propertyName_elem = etree.SubElement(compatibilityPropertyFilter_elem,"propertyName")
            propertyName_elem.text = cp_filter.propertyName

            for v in cp_filter.values:
                value_elem = etree.SubElement(compatibilityPropertyFilter_elem, "value")
                if v.number:
                    number_elem = etree.SubElement(value_elem, "number")
                    number_elem.text = v.number

                if v.text:
                    text_elem = etree.SubElement(value_elem, "text")
                    text_elem.text = v.text

                if v.url:
                    url_elem = etree.SubElement(value_elem, "URL")
                    url_elem.text = v.url

    #dataSet is a List
    if dataSet:
        for ds in dataSet:
            ds_elem = etree.SubElement(root, "dataSet")
            ds_elem.text = ds

    #disabledProductFilter is dict
    if disabledProductFilter:
        disabledProductFilter_elem = etree.SubElement(root, "disabledProductFilter")
        for key in disabledProductFilter.keys():
            key_elem = etree.SubElement(disabledProductFilter_elem, key)
            key_elem.text = disabledProductFilter[key]

    #paginationInput is Dict
    if paginationInput:
        for key in paginationInput.keys():
            key_elem = etree.SubElement(root, key)
            key_elem.text = paginationInput[key]

    #productIdentifier is dict
    productIdentifier_elem = etree.SubElement(root, "productIdentifier")
    for key in productIdentifier.keys():
        key_elem = etree.SubElement(productIdentifier_elem, key)
        key_elem.text = productIdentifier[key]

    #Really weirdly written API by eBay, sortOrder is used two times, confusing naming
    if sortOrder:
        for so in sortOrder:
            sortOrder_elem = etree.SubElement(root, "sortOrder")
            sortPriority_elem = etree.SubElement(sortOrder_elem,"sortPriority")
            sortPriority_elem.text = so.sortPriority

            subSortOrder_elem = etree.SubElement(sortOrder_elem, "sortOrder")
            order_elem = etree.SubElement(subSortOrder_elem, "order")
            order_elem.text = so.order
            propertyName_elem = etree.SubElement(subSortOrder_elem, "propertyName")
            propertyName_elem.text = so.propertyName

    request=etree.tostring(root, pretty_print=True)
    return get_response(getProductCompatibilities.__name__, request, encoding)


def findProducts(invocationId, \
                 dataset=None, \
                 datasetPropertyName=None, \
                 keywords=None, \
                 paginationInput=None, \
                 productStatusFilter=None, \
                 propertyFilter=None, \
                 sortOrder=None, \
                 encoding="JSON"):
    root = etree.Element("findProductsRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services")

    #Really messed up! : http://developer.ebay.com/DevZone/product/CallRef/findProducts.html#Samples

    request=etree.tostring(root, pretty_print=True)
    return get_response(findProducts.__name__, request, encoding)

def findProductsByCompatibility(encoding="JSON"):
    root = etree.Element("findProductsByCompatibilityRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services")

    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html

    request=etree.tostring(root, pretty_print=True)
    return get_response(findProductsByCompatibility.__name__, request, encoding)

def getProductDetails(encoding="JSON"):
    root = etree.Element("getProductDetailsRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services")

    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html

    request=etree.tostring(root, pretty_print=True)
    return get_response(getProductDetails.__name__, request, encoding)


def get_response(operation_name, data, encoding, **headers):
    config = get_config_store()
    app_name = config.get("keys", "app_name")
    endpoint = config.get("endpoints", "product")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-APPNAME": app_name,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    return data
