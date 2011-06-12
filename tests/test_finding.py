import unittest
from lxml import etree

from ebay.finding import *

encoding = "XML"
keywords = "ipod"
categoryId = "12"
productId = "1"
storeName = "store1"
affiliate = {"key":"value", "key2":"value"}
buyerPostalCode = "95112"
paginationInput = {"key":"value", "key2":"value"}
itemFilter = [{"key":"value", "key2":"value2"}, {"key3":"value3", "key4":"value4"}]
sortOrder = "so"
aspectFilter =  [{"key":"value", "key2":"value2"}, {"key3":"value3", "key4":"value4"}]
domainFilter = [{"key":"value", "key2":"value2"}, {"key3":"value3", "key4":"value4"}]
outputSelector =["os1", "os2", "os3"]


class TestFindingApi(unittest.TestCase):
    def test_getSearchKeywordsRecommendation(self):
        result = getSearchKeywordsRecommendation(keywords=keywords, encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Warning")


    def test_findItemsByKeywords(self):
        result = findItemsByKeywords(keywords=keywords, \
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
    unittest.main()
