import unittest
from lxml import etree

from ebay.best_match import *

#<!-- Standard Input Fields -->
siteResultsPerPage = "1"
ignoreFeatured = "false"
itemFilter = [{"paramName": "PriceMin", "paramValue": "50", "name": "Currency", "value": "USD"}]
outputSelector = ["FirstPageSummary", "SellerInfo"]
postSearchItemFilter = ["id1", "id2"]
postSearchSellerFilter = ["user1", "user2"]
siteResultsPerPage = "10"
entriesPerPage = "10"
paginationInput = {"entriesPerPage": "5", "pageNumber": "10"}

#<!-- Call-specific Input Fields -->
categoryId = "1"
keywords = "ipod"
productId = "123"
sellerUserName = "user1"


class TestBestMatchApi(unittest.TestCase):
    def test_keywords_findBestMatchItemDetailsAcrossStores(self):
        result = findBestMatchItemDetailsAcrossStores(keywords=keywords,\
                                                     siteResultsPerPage=siteResultsPerPage,\
                                                     categoryId=None, entriesPerPage=entriesPerPage,\
                                                     ignoreFeatured=ignoreFeatured,\
                                                     itemFilter=itemFilter,\
                                                     outputSelector=outputSelector,\
                                                     postSearchItemFilter=postSearchItemFilter,\
                                                     postSearchSellerFilter=postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_categoryId_findBestMatchItemDetailsAcrossStores(self):
        result = findBestMatchItemDetailsAcrossStores(keywords=None,\
                                                     siteResultsPerPage=siteResultsPerPage,\
                                                     categoryId=categoryId, entriesPerPage=entriesPerPage,\
                                                     ignoreFeatured=ignoreFeatured,\
                                                     itemFilter=itemFilter,\
                                                     outputSelector=outputSelector,\
                                                     postSearchItemFilter=postSearchItemFilter,\
                                                     postSearchSellerFilter=postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findBestMatchItemDetailsAdvanced(self):
        result = findBestMatchItemDetailsAdvanced(keywords=keywords,\
                                                  siteResultsPerPage=siteResultsPerPage,\
                                                  categoryId=None, \
                                                  entriesPerPage=entriesPerPage, \
                                                  ignoreFeatured=ignoreFeatured, \
                                                  itemFilter=itemFilter, \
                                                  outputSelector=outputSelector, \
                                                  postSearchItemFilter=postSearchItemFilter, \
                                                  postSearchSellerFilter=postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findBestMatchItemDetailsByCategory(self):
        result = findBestMatchItemDetailsByCategory(categoryId = categoryId, \
                                                    siteResultsPerPage = siteResultsPerPage, \
                                                    entriesPerPage = entriesPerPage, \
                                                    ignoreFeatured = ignoreFeatured, \
                                                    itemFilter = itemFilter, \
                                                    outputSelector = outputSelector, \
                                                    postSearchItemFilter = postSearchItemFilter, \
                                                    postSearchSellerFilter = postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findBestMatchItemDetailsByKeywords(self):
        result = findBestMatchItemDetailsByKeywords(keywords=keywords, \
                                                    siteResultsPerPage = siteResultsPerPage, \
                                                    entriesPerPage=entriesPerPage, \
                                                    ignoreFeatured=ignoreFeatured, \
                                                    itemFilter=itemFilter, \
                                                    outputSelector=outputSelector, \
                                                    postSearchItemFilter=postSearchItemFilter, \
                                                    postSearchSellerFilter=postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findBestMatchItemDetailsByProduct(self):
        result = findBestMatchItemDetailsByProduct(productId=productId, \
                                                   siteResultsPerPage=siteResultsPerPage, \
                                                   entriesPerPage=entriesPerPage, \
                                                   ignoreFeatured=ignoreFeatured, \
                                                   itemFilter=itemFilter, \
                                                   outputSelector=outputSelector, \
                                                   postSearchItemFilter=postSearchItemFilter, \
                                                   postSearchSellerFilter=postSearchSellerFilter)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_findBestMatchItemDetailsBySeller(self):
        result = findBestMatchItemDetailsBySeller(categoryId=categoryId, \
                                                  sellerUserName=sellerUserName, \
                                                  ignoreFeatured=ignoreFeatured, \
                                                  itemFilter=itemFilter, \
                                                  paginationInput=paginationInput)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    # def test_findBestMatchItemDetails(self):
        #     result = findBestMatchItemDetails()
        #     root = etree.fromstring(result)
        #     ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        #     self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
