import urllib2
from lxml import etree
from ConfigParser import ConfigParser
from utils import relative

config = ConfigParser()
config.read(relative("..", "config", "config.ini"))
dev_name = config.get("keys", "dev_name")
app_name = config.get("keys", "app_name")
cert_name = config.get("keys", "cert_name")
compatibility_level = config.get("call", "compatibility_level")
token = config.get("auth", "token")
endpoint = config.get("endpoints", "trading")

# Maps Ebay global ID TO Ebay site ID
map_site__global_id = {'EBAY-AT':16,'EBAY-AU':15,'EBAY-CH':193,'EBAY-DE':77,'EBAY-ENCA':2,'EBAY-ES':186,'EBAY-FR':71,'EBAY-FRBE':23,'EBAY-FRCA':210,'EBAY-GB':3,'EBAY-HK':201,'EBAY-IE':205,'EBAY-IN':203,'EBAY-IT':101,'EBAY-MOTOR':100,'EBAY-MY':207,'EBAY-NL':146,'EBAY-NLBE':123,'EBAY-PH':211,'EBAY-PL':212,'EBAY-SG':216,'EBAY-US':0}


def getCategories(global_id, category_parent=None,  level_limit=None, view_all_nodes=None, detail_level='ReturnAll', error_language=None, message_id=None, output_selectors=None, version=None, warning_level=None):
    root = etree.Element("GetCategoriesRequest", xmlns="urn:ebay:apis:eBLBaseComponents")
    add_standard_fields(root, detail_level, error_language, message_id, output_selectors, version, warning_level)
    sub_element(root, 'CategoryParent', category_parent)
    sub_element(root, 'CategorySiteID', map_site__global_id[global_id])
    sub_element(root, 'LevelLimit', level_limit)
    sub_element(root, 'ViewAllNodes', view_all_nodes)
    request = etree.tostring(root, pretty_print=True)
    return get_response('GetCategories', request)


def getItem(global_id, item_id, include_watch_count, detail_level='ReturnAll', error_language=None, message_id=None, output_selectors=None, version=None, warning_level=None):
    root = etree.Element("GetItemRequest", xmlns="urn:ebay:apis:eBLBaseComponents")
    add_standard_fields(root, detail_level, error_language, message_id, output_selectors, version, warning_level)
    sub_element(root, 'ItemID', item_id)
    sub_element(root, 'IncludeWatchCount', include_watch_count)
    request = etree.tostring(root, pretty_print=True)
    return get_response('GetItem', request)


# helpers-utils =======================================================================================================
def sub_element(elem, node_name, node_text):
    '''
    attaches a sub element to the given element
    '''
    if node_name == None or node_name == '':
        raise Exception('Element name is empty')
    if node_text == None:
        return
    sub_elem = etree.SubElement(elem, node_name)
    sub_elem.text = str(node_text)
    return sub_elem


def add_standard_fields(elem, detail_level, error_language, message_id, output_selectors, version, warning_level):
    '''
    theses fields are shared by all requests
    attaches standard fields to the given element
    '''

    #set token
    if token:
        credentials = etree.SubElement(elem, 'RequesterCredentials')
        sub_element(credentials, 'eBayAuthToken', token)

    sub_element(elem, "DetailLevel", detail_level)
    sub_element(elem, "ErrorLanguage", error_language)
    sub_element(elem, "MessageID", message_id)
    if output_selectors:
        for output_selector in output_selectors:
            sub_element(elem, "OutputSelector", output_selector)
    sub_element(elem, "Version", version)
    sub_element(elem, "WarningLevel", warning_level)


def get_response(operation_name, data, site_id=0, **headers):
    '''
    sends request and returns the response
    '''
    http_headers = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatibility_level,
                   "X-EBAY-API-DEV-NAME": dev_name,
                   "X-EBAY-API-APP-NAME": app_name,
                   "X-EBAY-API-CERT-NAME": cert_name,
                   "X-EBAY-API-CALL-NAME": operation_name,
                   "X-EBAY-API-SITEID": site_id
    }

    http_headers.update(headers)
    if (data.startswith('<?xml') == False):
        data = '<?xml version="1.0" encoding="utf-8"?>'+data

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
