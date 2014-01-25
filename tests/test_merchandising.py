import unittest
from lxml import objectify

from ebay.merchandising import *

keywords = "ipod"


class TestMerchandisingApi(unittest.TestCase):
    def test_getDeals(self):
        result = getDeals(keywords=keywords, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getMostWatchedItems(self):
        result = getMostWatchedItems(affiliate=None, maxResults=None,categoryId=None, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getRelatedCategoryItems(self):
        result = getRelatedCategoryItems(affiliate=None,
                                         maxResults=None, \                                        categoryId=None, \
                                       itemFilter=None, \
                                       itemId=None, \
                                       encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getSimilarItems(self):
        result = getSimilarItems(affiliate=None, \
                      maxResults=None, \
                      categoryId=None, \
                      categoryIdExclude=None, \
                      endTimeFrom=None, \
                      endTimeTo=None, \
                      itemFilter=None, \
                      itemId=None, \
                      listingType=None, \
                       axPrice=None, \
                        encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


    def test_getTopSellingProducts(self):
        result = getTopSellingProducts(affiliate=None, maxResults=None, encoding="XML")
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
