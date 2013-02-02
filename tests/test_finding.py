import unittest
from lxml import etree

from ebay.finding import *

encoding = "XML"
keywords = "ipod"
categoryId = "12"
productId = "1"
storeName = "store1"
#This information is encoded in URLs so the affiliate can get his commission. 
affiliate = {"networkId":"9", "trackingId":"1234567890"}
buyerPostalCode = "95112"
paginationInput = {"entriesPerPage": "5", "pageNumber" : "1"}
#http://developer.ebay.com/DevZone/finding/CallRef/types/ItemFilterType.html
itemFilter = [{"name":"MaxPrice", "value":"100", 
               "paramName":"Currency", "paramValue":"EUR"}, 
              {"name":"MinPrice", "value":"50", 
               "paramName":"Currency", "paramValue":"EUR"}]
#http://developer.ebay.com/DevZone/finding/CallRef/findItemsByKeywords.html#Request.sortOrder
sortOrder = "EndTimeSoonest"
#TODO: These values
aspectFilter =  [{"key":"value", "key2":"value2"}, {"key3":"value3", "key4":"value4"}]
domainFilter = [{"key":"value", "key2":"value2"}, {"key3":"value3", "key4":"value4"}]
outputSelector =["os1", "os2", "os3"]


#TODO: test if results are actually useful
class TestFindingApi(unittest.TestCase):
    def test_getSearchKeywordsRecommendation(self):
        result = getSearchKeywordsRecommendation(keywords="eipod", encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findItemsByKeywords(self):
        result = findItemsByKeywords(
                        keywords=keywords, \
                        affiliate=affiliate, \
                        buyerPostalCode=buyerPostalCode, \
                        paginationInput=paginationInput, \
                        sortOrder=sortOrder, \
#                        aspectFilter=aspectFilter, \
#                        domainFilter=domainFilter, \
                        itemFilter=itemFilter, \
#                        outputSelector=outputSelector, \
                        encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findItemsByCategory(self):
        result = findItemsByCategory(categoryId=categoryId, \
                        affiliate=affiliate, \
                        buyerPostalCode=buyerPostalCode, \
                        sortOrder=sortOrder, \
                        paginationInput = paginationInput, \
                        aspectFilter=aspectFilter, \
                        domainFilter=domainFilter, \
                        itemFilter=itemFilter, \
                        outputSelector=outputSelector, \
                        encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findItemsAdvanced(self):
        result = findItemsAdvanced(keywords=keywords, \
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
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findItemsByProduct(self):
        result = findItemsByProduct(keywords=keywords, \
                       productId=productId, \
                       affiliate=affiliate, \
                       buyerPostalCode=buyerPostalCode, \
                       paginationInput= paginationInput, \
                       sortOrder=sortOrder, \
                       itemFilter=itemFilter, \
                       outputSelector=outputSelector, \
                       encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Failure")


    def test_findItemsIneBayStores(self):
        result = findItemsIneBayStores(keywords=keywords, \
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


    def test_getHistograms(self):
        result = getHistograms(categoryId=categoryId, encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")

if __name__ == '__main__':
    #Run single test manually
    t = TestFindingApi("test_findItemsByKeywords")
    t.test_findItemsByKeywords()
    
    #unittest.main()
