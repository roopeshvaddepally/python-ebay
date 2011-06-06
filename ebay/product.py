import urllib2
from lxml import etree

from ConfigParser import ConfigParser
from utils import relative

def findCompatibilitiesBySpecification(specification, categoryId=None, compatibilityPropertyFilter=None, dataSet=None, datasetPropertyName=None, exactMatch=None, paginationInput=None, sortOrder=None):
    root = etree.Element("findCompatibilitiesBySpecificationRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"

    if categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = categoryId
    
    #specification should be an object: FIX IT
    for spec in specification:
        specification_elem = etree.SubElement(root, "specification")
        propertyName_elem = etree.SubElement(specification_elem,"propertyName")
        propertyName_elem.text = spec_propertyName 
        
        for value in spec:
            value_elem = etree.SubElement(specification_elem, "value")
            for key in value:
                key_elem = etree.SubElement(value_elem, key)
                keyValue_elem = etree.SubElement(key_elem, "value")
                keyValue_elem.text = value[key]

    #compatibilityPropertyFilter should be an object: FIX IT
    if compatibilityPropertyFilter_propertyName and compatibilityPropertyFilter:
        for c_filter in compatibilityPropertyFilter:
        c_filter_elem = etree.SubElement(root, "compatibilityPropertyFilter")
        propertyName_elem = etree.SubElement(c_filter_elem,"propertyName")
        propertyName_elem.text = compatibilityPropertyFilter_propertyName
        
        for value in c_filter:
            value_elem = etree.SubElement(c_filter_elem, "value")
            for key in value:
                key_elem = etree.SubElement(value_elem, key)
                keyValue_elem = etree.SubElement(key_elem, "value")
                keyValue_elem.text = value[key]

    
    #dataSet is a List
    if dataSet:
        for ds in dataSet:
            ds_elem = etree.SubElement(root, "dataSet")
            ds_elem.text = dataSet

    #datasetPropertyName is a List
    if datasetPropertyName:
        for dpn in datasetPropertyName:
            dpn_elem = etree.SubElement(root, "datasetPropertyName")
            dpn_elem = datasetPropertyName

    if exactMatch:
        exactMatch_elem = etree.SubElement(root, "exactMatch")
        exactMatch_elem.text = exactMatch
        
    #paginationInput is Dict
    if paginationInput:
        for key in paginationInput.keys():
            key_elem = etree.SubElement(root, key)
            key_elem.text = paginationInput[key]
    
    #sortOrder should be an object: FIX IT 
    if sortOrder:
        
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(findCompatibilitiesBySpecification.__name__, request)
    
def findProducts(invocationId, dataset=None, datasetPropertyName=None, keywords=None, paginationInput=None, productStatusFilter=None, propertyFilter=None, sortOrder=None):
    root = etree.Element("findProductsRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"

    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html
    
    productSearch_elem = etree.SubElement(root, "productSearch")
    invocationId_elem = etree.SubElement(productSearch_elem, "invocationId")
    invocationId_elem.text = invocationId

    #dataSet is a List
    if dataSet:
        for ds in dataSet:
            ds_elem = etree.SubElement(root, "dataSet")
            ds_elem.text = dataSet

    #datasetPropertyName is a List
    if datasetPropertyName:
        for dpn in datasetPropertyName:
            dpn_elem = etree.SubElement(root, "datasetPropertyName")
            dpn_elem = datasetPropertyName

    #paginationInput is Dict
    if paginationInput:
        for key in paginationInput.keys():
            key_elem = etree.SubElement(root, key)
            key_elem.text = paginationInput[key]

    #productStatusFilter is dict

    #propertyFilter is list of dict

    #sortOrder is dict
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(findProducts.__name__, request)

def findProductsByCompatibility():
    root = etree.Element("findProductsByCompatibilityRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"
    
    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(findProductsByCompatibility.__name__, request)

def getProductCompatibilities(datasetPropertyName, productIdentifier, applicationPropertyFilter=None, dataset=None, disabledProductFilter=None, paginationInput=None, productIdentifier=None, sortOrder=None):
    root = etree.Element("findProductsByCompatibilityRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"
   
    #datasetPropertyName is a List
    if datasetPropertyName:
        for dpn in datasetPropertyName:
            dpn_elem = etree.SubElement(root, "datasetPropertyName")
            dpn_elem = datasetPropertyName
            
    #applicationPropertyFilter is list of dicts
    
    #dataSet is a List
    if dataSet:
        for ds in dataSet:
            ds_elem = etree.SubElement(root, "dataSet")
            ds_elem.text = dataSet
            
    #disabledProductFilter is dict

    #paginationInput is Dict
    if paginationInput:
        for key in paginationInput.keys():
            key_elem = etree.SubElement(root, key)
            key_elem.text = paginationInput[key]

    #productIdentifier is dict

    #sortOrder is list of dicts
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(getProductCompatibilities.__name__, request)
    
def getProductDetails():
    root = etree.Element("getProductDetailsRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"
    
    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(getProductDetails.__name__, request)
    

def get_response(operation_name, data):
    endpoint='http://svcs.sandbox.ebay.com/services/marketplacecatalog/ProductService/v1'
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    access_token = config.get("auth", "token")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-TOKEN": access_token}
    
    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data