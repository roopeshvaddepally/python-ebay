#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from os.path import join, dirname, abspath
# import urllib2
from six import PY3 as PYTHON3
# from ConfigParser import ConfigParser
from six.moves.configparser import ConfigParser
import requests
from lxml import etree
import base64
#import codecs
import json
import shutil
import os


# http://python-future.org/compatible_idioms.html
# urllib module
# urllib is the hardest module to use from Python 2/3 compatible code.

# Python 2 and 3: alternative 4 (modified)
if PYTHON3:
    from urllib.request import urlopen, Request
else:
    from urllib2 import urlopen, Request


def get_endpoint_response(endpoint_name, operation_name, data, encoding, 
                          **headers):
    config = get_config_store()
    endpoint = config.get("endpoints", endpoint_name)
    app_name = config.get("keys", "app_name")
    dev_name = config.get("keys", "dev_name")
    cert_name = config.get("keys", "cert_name")
    compatibility_level = config.get("call", "compatibility_level")
    siteId = config.get("call", "siteid")

    http_headers = { "X-EBAY-API-COMPATIBILITY-LEVEL" : compatibility_level,
                "X-EBAY-API-DEV-NAME" : dev_name,
                "X-EBAY-API-APP-NAME" : app_name,
                "X-EBAY-API-CERT-NAME": cert_name,
                "X-EBAY-API-CALL-NAME": operation_name,
                "X-EBAY-API-SITEID" : siteId,
                "Content-Type" : "text/xml" }

    http_headers.update(headers)

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    return data

def get_endpoint_response_with_file(endpoint_name, operation_name, fobj, data,
                                    encoding, **headers):
    config = get_config_store()
    endpoint = config.get("endpoints", endpoint_name)
    app_name = config.get("keys", "app_name")
    dev_name = config.get("keys", "dev_name")
    cert_name = config.get("keys", "cert_name")
    compatibility_level = config.get("call", "compatibility_level")
    siteId = config.get("call", "siteid")

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

CONFIG_STORE = None

def set_config_file(filename):
    """
    Change the configuration file. 
    Use configuration file in non standard location.
    """
    global CONFIG_STORE
    CONFIG_STORE = ConfigParser()
    CONFIG_STORE.read(filename)

def get_config_store():
    """
    Return storage object with configuration values.
    The returned object is a ConfigParser, that is queried like this::
    
        key = store.get("section", "key")
    """
    global CONFIG_STORE
    if CONFIG_STORE is None:
        CONFIG_STORE = ConfigParser()
        CONFIG_STORE.read(relative("config.ini"))
        
    return CONFIG_STORE

def write_config_example(dst=None):
    """
    Write an example configuration file for python-ebay.
    
    * If **dst** is None, the file is written into the current directory,
      and named ``config.ini.example``.
    * If **dst** is an existing directory, the file is written into this 
      directory, and named ``config.ini.example``.
    * If **dst** is a file name, the example is written into a file with this
      name.
    """
    if dst is None:
        dst = os.getcwd()
    config_example_path = relative("config.ini.example")
    shutil.copy(config_example_path, dst)


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
    imgur_key = get_config_store().get("keys", "imgur_key")
    fobj = open(filepath, "rb")
    bimage = fobj.read()  #again, not string data, but binary data
    fobj.close()
    b64image = base64.b64encode(bimage)
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

