#!/usr/bin/env pythin
#-*- coding: utf-8 -*-
import sys
from os.path import join, dirname, abspath
import urllib2
from ConfigParser import ConfigParser
import requests
from lxml import etree
import base64
import codecs
import json

def get_endpoint_response(endpoint_name, operation_name, data, encoding, **headers):

    config_dict = get_config_value({ ("endpoints", endpoint_name) : "",
                    ("keys", "app_name") : "",
                    ("keys", "dev_name") : "",
                    ("keys", "cert_name") : "",
                    ("call", "siteid") : "",
                    ("call", "compatibility_level") : "", })
    
    
    endpoint = config_dict[("endpoints", endpoint_name)]
    app_name = config_dict[("keys", "app_name")]
    dev_name = config_dict[("keys", "dev_name")]
    cert_name = config_dict[("keys", "cert_name")]
    compatibility_level = config_dict[("call", "compatibility_level")]
    siteId = config_dict[("call", "siteid")]

    http_headers = { "X-EBAY-API-COMPATIBILITY-LEVEL" : compatibility_level,
                "X-EBAY-API-DEV-NAME" : dev_name,
                "X-EBAY-API-APP-NAME" : app_name,
                "X-EBAY-API-CERT-NAME": cert_name,
                "X-EBAY-API-CALL-NAME": operation_name,
                "X-EBAY-API-SITEID" : siteId,
                "Content-Type" : "text/xml" }

    http_headers.update(headers)

    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data

def get_endpoint_response_with_file(endpoint_name, operation_name, fobj, data,
        encoding, **headers):
    config_dict = get_config_value({ ("endpoints", endpoint_name) : "",
                    ("keys", "app_name") : "",
                    ("keys", "dev_name") : "",
                    ("keys", "cert_name") : "",
                    ("call", "siteid") : "",
                    ("call", "compatibility_level") : "", })
    
    
    endpoint = config_dict[("endpoints", endpoint_name)]
    app_name = config_dict[("keys", "app_name")]
    dev_name = config_dict[("keys", "dev_name")]
    cert_name = config_dict[("keys", "cert_name")]
    compatibility_level = config_dict[("call", "compatibility_level")]
    siteId = config_dict[("call", "siteid")]

    http_headers = { "X-EBAY-API-COMPATIBILITY-LEVEL" : compatibility_level,
                "X-EBAY-API-DEV-NAME" : dev_name,
                "X-EBAY-API-APP-NAME" : app_name,
                "X-EBAY-API-CERT-NAME": cert_name,
                "X-EBAY-API-CALL-NAME": operation_name,
                "X-EBAY-API-SITEID" : siteId,
                "X-EBAY-API-DETAIL-LEVEL": "0",
                "Content-Type" : "multipart/form-data" }

    http_headers.update(headers)

    files = {'file': ('image', fobj)}
    dataload = { 'body': data }
    res = requests.post(endpoint, files=files, data=dataload,
                        headers=http_headers)
    return res.text

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)

def get_config_value(configTupleDict):
    """ configTupleDict should be a dictionary with a tuple key
    where the value will be filled by this function
    (i.e. configTupleDict = { ("section", "key") : "actual value from config goes here", }
    """
    if configTupleDict:
        config = ConfigParser()
        config.read(relative("config.ini"))
        #fill the dict of tuples
        for curItem in configTupleDict:
            configTupleDict[curItem] = config.get(curItem[0],curItem[1])
            

    return configTupleDict

class Value(object):
    def __init__(self,
                 number=None,
                 text=None,
                 url=None):
        self.number = number
        self.text = text
        self.url = url


class Specification(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class CompatibilityPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class ApplicationPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []


class SortOrder(object):
    def __init__(self, sortPriority, order, propertyName):
        self.sortPriority = sortPriority
        self.order = order
        self.propertyName = propertyName

def add_e(parent, key, val=None):
    child = etree.SubElement(parent, key)
    if val:
        child.text = str(val)
    return child


def imgur_post(filepath):
    imgur_key = get_config_value({("keys", "imgur_key"): "", }
        )[("keys", "imgur_key")]
    fobj = open(filepath, "rb")
    bin = fobj.read()  #again, not string data, but binary data
    fobj.close()
    b64image = base64.b64encode(bin)
    payload = {
        'key': imgur_key,
        'image': b64image,
        'title': 'an upload'
    }
    endpoint = 'http://api.imgur.com/2/upload.json'
    r = requests.post(endpoint, data=payload)
    j = json.loads(r.text)
    url = j['upload']['links']['original']
    sys.stderr.write('Upload Success!    %s    %s\n' % (filepath, url))
    return url

