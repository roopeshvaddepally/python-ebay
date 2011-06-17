import unittest
from lxml import objectify

from ebay.shopping import *

class TestShoppingApi(unittest.TestCase):
    def test_FindProducts(self):
        result = FindProducts()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_FindHalfProducts(self):
        result = FindHalfProducts()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetSingleItem(self):
        result = GetSingleItem()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetItemStatus(self):
        result = GetSingleItem()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetShippingCosts(self):
        result = GetShippingCosts()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetMultipleItems(self):
        result = GetMultipleItems()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetUserProfile(self):
        result = GetUserProfile()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_FindPopularSearches(self):
        result = FindPopularSearches()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_FindPopularItems(self):
        result = FindPopularItems()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_FindReviewsandGuides(self):
        result = FindReviewsandGuides()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GetCategoryInfo(self):
        result = GetCategoryInfo()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")

    def test_GeteBayTime(self):
        result = GeteBayTime()
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
