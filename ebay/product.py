import urllib2
from lxml import etree

from ConfigParser import ConfigParser
from utils import relative

def findCompatibilitiesBySpecification(specification, categoryId=None, compatibilityPropertyFilter=None, dataSet=None, datasetPropertyName=None, exactMatch=None, paginationInput=None, sortOrder=None):
    root = etree.Element("findCompatibilitiesBySpecificationRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"

    #specification is a List of Dicts
    

    #compatibilityPropertyFilter is List of dicts

    #dataSet is a List

    #datasetPropertyName is a List

    #paginationInput is Dict

    #sortOrder is list of dicts
    
    
    request=etree.tostring(root, pretty_print=True)
    return get_response(findCompatibilitiesBySpecification.__name__, request)
    
def findProducts(invocationId, dataset=None, datasetPropertyName=None, keywords=None, paginationInput=None, productStatusFilter=None, propertyFilter=None, sortOrder=None):
    root = etree.Element("findProductsRequest", xmlns="http://www.ebay.com/marketplace/marketplacecatalog/v1/services"

    #Problem with getProductDetails, findProductsByCompatibility and findProducts method: http://developer.ebay.com/DevZone/product/CallRef/index.html
    
    productSearch_elem = etree.SubElement(root, "productSearch")
    invocationId_elem = etree.SubElement(productSearch_elem, "invocationId")
    invocationId_elem.text = invocationId

    #dataset is a List

    #datasetPropertyName is List

    #paginationInput is dict

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
    
    #applicationPropertyFilter is list of dicts
    
    #dataset is list

    #disabledProductFilter is dict

    #paginationInput is dict

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