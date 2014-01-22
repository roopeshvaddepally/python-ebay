"""
Tests for package ``ebay.finding``

These tests are designed to work on the production system, not on Ebay's 
sandbox.

This test uses a custom configuration file ``config-test1.ini`` inside the 
``tests/`` directory. It can be most easily created, by first copying::

     mv config-test1.ini.example  config-test1.ini
     
Then filling in user and application keys into ``config-test1.ini``.
"""

import os.path as path 
import unittest
from lxml import etree

from ebay.utils import set_config_file
from ebay.finding import (getSearchKeywordsRecommendation, getHistograms,
                          findItemsAdvanced, findItemsByCategory, 
                          findItemsByKeywords, findItemsByProduct,
                          findItemsIneBayStores)


def relative(*path_fragments):
    'Create a file path that is relative to the location of this file.'
    return path.abspath(path.join(path.dirname(__file__), *path_fragments))

#Tell python-ebay to use the custom configuration file
set_config_file(relative("config-test1.ini"))


#Definitions of the various arguments of the finding API.
encoding = "XML" #default "JSON": Output encoding
keywords = "ipod"
#Get category IDs with function: `ebay.shopping.GetCategoryInfo`
categoryId = "73839" #iPods & MP3 Players
productId = "77767691" #iPod nano 5th gen. Black. Each product has unique ID.
storeName = "Fab Finds 4 U" #A big store that won't go away soon.
#This information is encoded in URLs so the affiliate can get his commission. 
affiliate = {"networkId":"9", "trackingId":"1234567890"}
buyerPostalCode = "10027" #central New York City, USA
#Set number of results per call (here 10). Get additional results by 
#increasing page number.
paginationInput = {"entriesPerPage": "10", "pageNumber" : "1"}
#http://developer.ebay.com/DevZone/finding/CallRef/types/ItemFilterType.html
itemFilter = [{"name":"MaxPrice", "value":"100", 
               "paramName":"Currency", "paramValue":"EUR"}, 
              {"name":"MinPrice", "value":"50", 
               "paramName":"Currency", "paramValue":"EUR"}]
#http://developer.ebay.com/DevZone/finding/CallRef/findItemsByKeywords.html#Request.sortOrder
sortOrder = "EndTimeSoonest"
aspectFilter =  [{"aspectName":"Color", "aspectValueName":"Black"}, 
                 {"aspectName":"", "aspectValueName":""}]
#Multiple domain filters are currently unsupported
domainFilter = [{"domainName":"Other_MP3_Players"}] 
#http://developer.ebay.com/DevZone/finding/CallRef/types/OutputSelectorType.html
outputSelector =["StoreInfo", "SellerInfo", "AspectHistogram"]


class TestFindingApi(unittest.TestCase):
    def test_getSearchKeywordsRecommendation(self):
        result = getSearchKeywordsRecommendation(keywords="eipod", encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        keyword = root.find("{http://www.ebay.com/marketplace/search/v1/services}keywords").text
        self.assertEqual(keyword, "ipod")
        

    def test_findItemsByKeywords(self):
        result = findItemsByKeywords(
                        keywords=keywords, \
                        affiliate=affiliate, \
                        buyerPostalCode=buyerPostalCode, \
                        paginationInput=paginationInput, \
                        sortOrder=sortOrder, \
                        aspectFilter=aspectFilter, \
                        domainFilter=domainFilter, \
                        itemFilter=itemFilter, \
                        outputSelector=outputSelector, \
                        encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        #Number of Items between 0 and 10, because of paginationInput
        res_items = root.find("{http://www.ebay.com/marketplace/search/v1/services}searchResult")
        self.assertTrue(0 <= len(res_items) <= 10)


    def test_findItemsByCategory(self):
        result = findItemsByCategory(
                        categoryId=categoryId, \
                        affiliate=affiliate, \
                        buyerPostalCode=buyerPostalCode, \
                        sortOrder=sortOrder, \
                        paginationInput = paginationInput, \
                        aspectFilter=aspectFilter, \
                        domainFilter=domainFilter, \
                        itemFilter=itemFilter, \
                        outputSelector=outputSelector, \
                        encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        #Number of Items between 0 and 10, because of paginationInput
        res_items = root.find("{http://www.ebay.com/marketplace/search/v1/services}searchResult")
        self.assertTrue(0 <= len(res_items) <= 10)


    def test_findItemsAdvanced(self):
        result = findItemsAdvanced(
                      keywords=keywords, \
                      categoryId=categoryId, \
                      affiliate=affiliate, \
                      buyerPostalCode=buyerPostalCode, \
                      paginationInput= paginationInput, \
                      sortOrder=sortOrder, \
                      aspectFilter=aspectFilter, \
                      domainFilter=domainFilter, \
                      itemFilter=itemFilter, \
                      outputSelector=outputSelector, \
                      encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        #Number of Items between 0 and 10, because of paginationInput
        res_items = root.find("{http://www.ebay.com/marketplace/search/v1/services}searchResult")
        self.assertTrue(0 <= len(res_items) <= 10)


    def test_findItemsByProduct(self):
        result = findItemsByProduct(
                       keywords=keywords, \
                       productId=productId, \
                       affiliate=affiliate, \
                       buyerPostalCode=buyerPostalCode, \
                       paginationInput= paginationInput, \
                       sortOrder=sortOrder, \
                       itemFilter=itemFilter, \
                       outputSelector=outputSelector, \
                       encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Failure") 


    def test_findItemsIneBayStores(self):
        result = findItemsIneBayStores(
                          keywords=keywords, \
                          storeName=storeName, \
                          affiliate=affiliate, \
                          buyerPostalCode=buyerPostalCode, \
                          paginationInput=paginationInput, \
                          sortOrder=sortOrder, \
                          aspectFilter=aspectFilter, \
                          domainFilter=domainFilter, \
                          itemFilter=itemFilter, \
                          outputSelector=outputSelector, \
                          encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")
        #Number of Items between 0 and 10, because of paginationInput
        res_items = root.find("{http://www.ebay.com/marketplace/search/v1/services}searchResult")
        self.assertTrue(0 <= len(res_items) <= 10)


    def test_getHistograms(self):
        result = getHistograms(categoryId=categoryId, encoding=encoding)
#        print result
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
#    #Run single test manually. 
#    t = TestFindingApi("test_findItemsByProduct")
#    t.test_findItemsByProduct()
    
    unittest.main()
