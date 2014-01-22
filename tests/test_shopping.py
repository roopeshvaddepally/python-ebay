"""
Tests for package ``ebay.shopping``.


Configuration
=============

This test script uses a custom configuration file ``config-test1.ini`` 
inside directory ``tests/``. It can be most easily created, by first copying::

     mv config-test1.ini.example  config-test1.ini
     
Then filling in user and application keys into ``config-test1.ini``.


These tests are designed to work on the production system, not on Ebay's 
sand box.

Some tests also call functions from the Finding API. Therefore a broken Finding
API will also cause breakage here.
"""

import os.path as path 
import unittest
from lxml import objectify

from ebay.utils import set_config_file
from ebay.finding import findItemsByKeywords
from ebay.shopping import *


def find_item_ids(keywords):
    "Return a list of, at most 10, valid item IDs."
    result = findItemsByKeywords(keywords, 
                                 paginationInput = {"entriesPerPage": "10", 
                                                    "pageNumber" : "1"}, 
                                 encoding="XML")
#    print result
    root = objectify.fromstring(result)
    ack = root.ack.text
    assert ack == "Success" or ack == "Warning"
    
    items = root.searchResult.item
    item_ids = []
    for itemi in items:
        itemi_id = itemi.itemId.text
        item_ids.append(itemi_id)
#    print item_ids
    return item_ids
    
def relative(*path_fragments):
    'Create a file path that is relative to the location of this file.'
    return path.abspath(path.join(path.dirname(__file__), *path_fragments))


#Tell python-ebay to use the custom configuration file
set_config_file(relative("config-test1.ini"))


#Definitions of the various arguments of the shopping API.
#Keywords for search.
keywords = "ipod" 
#Only return information for items that are available.
available_items = True 
#Maximal number of entries in reply 
max_entries = 10 
#Specify the amount of information that is returned. 
#  If ``None`` a small number of default fields is returned.
#  Can consist of multiple words separated by commas. Possible values:
#    Details, Description, TextDescription, ShippingCosts, ItemSpecifics,
#    Variations, Compatibility
include_selector = "ShippingCosts"
##String that identifies the destination country. USA: "US", Germany: "DE"
##http://developer.ebay.com/DevZone/shopping/docs/CallRef/types/CountryCodeType.html
#destination_country_code = "US"
##Postal code, country specific. For example "52068": eastern Aachen, Germany
#destination_postal_code = "10027" #central New York City, USA
##Return more detailed information
#details = False
##Number of items that should be shipped together.
#quantity_sold = 1
#Encoding of the returned data, possible values "JSON", "XML"
encoding = "XML" 


class TestShoppingApi(unittest.TestCase):
    def test_FindProducts(self):
        """
        http://developer.ebay.com/Devzone/shopping/docs/CallRef/FindProducts.html
        """
        result = FindProducts(query=keywords, 
                              available_items=available_items, 
                              max_entries=max_entries,
                              encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        product = root.Product
        self.assertTrue(len(product) == 10, 
                        "``product`` container has unexpected length.")
        product_id_0 = product[0].ProductID.text
        self.assertTrue(int(product_id_0) != 0, 
                        "``product_id_0`` must be string representation "
                        "of an integer.")

    def test_FindHalfProducts(self):
        """
        TODO: Test call with all keywords.
        
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/FindHalfProducts.html
        """
        result = FindHalfProducts(query=keywords, 
                                  max_entries=max_entries, 
                                  product_type=None, 
                                  product_value=None, 
                                  include_selector=None,
                                  encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        product = root.Products.Product
        self.assertTrue(len(product) == 10, 
                        "``product`` container has unexpected length.")
        product_id_0 = product[0].ProductID.text
        self.assertTrue(int(product_id_0) != 0, 
                        "``product_id_0`` must be string representation "
                        "of an integer.")

    def test_GetSingleItem(self):
        """
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetSingleItem.html
        """
        item_ids = find_item_ids(keywords)
        
        result = GetSingleItem(item_ids[0], 
                               include_selector=include_selector,
                               encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

        title = root.Item.Title.text
        price = root.Item.ConvertedCurrentPrice.text
        self.assertTrue(len(title) > 0, 
                        "The title is most probably a string with length > 0.")
        self.assertTrue(float(price) > 0, 
                        "The price is the string representation od a float. "
                        "It should be > 0.")
        
    def test_GetItemStatus(self):
        """
        developer.ebay.com/DevZone/shopping/docs/CallRef/GetItemStatus.html
        """
        item_ids = find_item_ids(keywords)
        
        result = GetItemStatus(item_id=item_ids[0],
                               encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        time_left = root.Item[0].TimeLeft.text
        price = root.Item[0].ConvertedCurrentPrice.text
        self.assertTrue(len(time_left) > 0, 
                        "The time left is most probably a string with length > 0.")
        self.assertTrue(float(price) > 0, 
                        "The price is the string representation od a float. "
                        "It should be > 0.")
        
    def test_GetShippingCosts(self):
        """
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetShippingCosts.html
        """
        item_ids = find_item_ids(keywords)
        
        result = GetShippingCosts(item_id=item_ids[0], 
                                  destination_country_code="US", 
                                  destination_postal_code="10027", 
                                  details=True, 
                                  quantity_sold=1, 
                                  encoding=encoding)
        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        shcost = root.ShippingCostSummary.ShippingServiceCost.text 
        self.assertTrue(float(shcost) >= 0, 
                        "Shipping cost must be a string that represents a "
                        "float, and be positive.")

    def test_GetMultipleItems(self):
        """
        http://developer.ebay.com/Devzone/shopping/docs/CallRef/GetMultipleItems.html
        """
        item_ids = find_item_ids(keywords)
        item_ids_str = ",".join(item_ids)
        
        result = GetMultipleItems(item_id=item_ids_str, 
                                  include_selector=include_selector,
                                  encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

        items = root.Item
        for itemi in items:
            title = itemi.Title.text
            price = itemi.ConvertedCurrentPrice.text
            self.assertTrue(len(title) > 0, 
                            "The title is most probably a string with length > 0.")
            self.assertTrue(float(price) > 0, 
                            "The price is the string representation od a float. "
                            "It should be > 0.")

    def test_GetUserProfile(self):
        result = GetUserProfile(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_FindPopularSearches(self):
        result = FindPopularSearches(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_FindPopularItems(self):
        result = FindPopularItems(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_FindReviewsandGuides(self):
        result = FindReviewsandGuides(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_GetCategoryInfo(self):
        result = GetCategoryInfo(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_GeteBayTime(self):
        result = GeteBayTime(encoding=encoding)
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        ebay_time = root.Timestamp.text 
        print ebay_time


if __name__ == '__main__':
    #Run single test manually. 
    t = TestShoppingApi("test_GetMultipleItems")
    t.test_GetMultipleItems()
    
#    unittest.main()
