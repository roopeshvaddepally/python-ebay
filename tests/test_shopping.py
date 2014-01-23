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
    
    item_ids = []
    for itemi in root.searchResult.item:
        item_ids.append(itemi.itemId.text)
#    print item_ids
    return item_ids
    
def relative(*path_fragments):
    'Create a file path that is relative to the location of this file.'
    return path.abspath(path.join(path.dirname(__file__), *path_fragments))


#Tell python-ebay to use the custom configuration file
set_config_file(relative("config-test1.ini"))


class TestShoppingApi(unittest.TestCase):
    def test_FindProducts(self):
        """
        http://developer.ebay.com/Devzone/shopping/docs/CallRef/FindProducts.html
        """
        result = FindProducts(query="ipod", 
                              available_items=True, 
                              max_entries=10,
                              encoding="XML")
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
        result = FindHalfProducts(query="ipod", 
                                  max_entries=10, 
                                  product_type=None, 
                                  product_value=None, 
                                  include_selector=None,
                                  encoding="XML")
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
        item_ids = find_item_ids("ipod")
        
        result = GetSingleItem(item_ids[0], 
                               include_selector="ShippingCosts",
                               encoding="XML")
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
        item_ids = find_item_ids("ipod")
        
        result = GetItemStatus(item_id=item_ids[0],
                               encoding="XML")
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
        item_ids = find_item_ids("ipod")
        
        result = GetShippingCosts(item_id=item_ids[0], 
                                  destination_country_code="US", 
                                  destination_postal_code="10027", 
                                  details=True, 
                                  quantity_sold=1, 
                                  encoding="XML")
#        print result
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
        item_ids = find_item_ids("ipod")
        item_ids_str = ",".join(item_ids)
        
        result = GetMultipleItems(item_id=item_ids_str, 
                                  include_selector="ShippingCosts",
                                  encoding="XML")
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
        """
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetUserProfile.html
        """
        result = GetUserProfile(user_id=
                                #ID of deleted user
                                "bfafcc239c92d6404cd33a13648076d324750574", 
                                include_selector="Details", 
                                encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        score = root.User.FeedbackScore.text 
        status = root.User.Status.text
        self.assertTrue(int(score) > 600, 
                        "Score must represent an integer. "
                        "This user's score is above 600")
        self.assertTrue(status == "Deleted", "This is a deleted account.")
        
        
    def test_FindPopularSearches(self):
        """
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/FindPopularSearches.html
        """
        result = FindPopularSearches(query="ipod,car", 
                                     category_id=None,
                                     encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

        query = root.PopularSearchResult[0].QueryKeywords.text 
        alternative = root.PopularSearchResult[0].AlternativeSearches.text
        related = root.PopularSearchResult[0].RelatedSearches.text
        self.assertTrue(len(query)>1)
        self.assertTrue(len(alternative)>1)
        self.assertTrue(len(related)>1)
        
        
    def test_FindPopularItems(self):
        """
        developer.ebay.com/DevZone/shopping/docs/CallRef/FindPopularItems.html
        """
        result = FindPopularItems(query="ipod,car", 
                                  category_id_exclude=None,
                                  encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

        items = root.ItemArray.Item
        price = items[0].ConvertedCurrentPrice.text
        title = items[0].Title.text
        self.assertTrue(len(items) > 1, "eBay returns multiple popular items.")
        self.assertTrue(float(price) > 0, "Price is a float.")
        self.assertTrue(len(title) > 10, "``title`` is a somewhat long string.")
        

    def test_FindReviewsandGuides(self):
        """
        http://developer.ebay.com/Devzone/shopping/docs/CallRef/FindReviewsAndGuides.html
        """
        result = FindReviewsandGuides(category_id="29997", 
                                      product_id=None,
                                      encoding="XML")
        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

    def test_GetCategoryInfo(self):
        """
        http://developer.ebay.com/DevZone/shopping/docs/CallRef/GetCategoryInfo.html
        """
        result = GetCategoryInfo(category_id="73839", #iPods & MP3 Players
                                 include_selector=None, 
                                 encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")

        cat_id = root.CategoryArray.Category.CategoryID.text
        cat_name = root.CategoryArray.Category.CategoryName.text 
        self.assertTrue(cat_id == "73839", "Must be same ID as in query.")
        self.assertTrue(cat_name.startswith("iPod"), 
                        "Category name is: 'iPods & MP3 Player'")
        

    def test_GeteBayTime(self):
        """
        http://developer.ebay.com/Devzone/shopping/docs/CallRef/GeteBayTime.html
        """
        result = GeteBayTime(encoding="XML")
#        print result
        root = objectify.fromstring(result)
        ack = root.Ack.text
        self.assertEqual(ack, "Success")
        
        ebay_time = root.Timestamp.text 
        print ebay_time
        self.assertTrue(len(ebay_time) > 10, 
                        "eBay time is a somewhat long string.")
        

if __name__ == '__main__':
#    #Run single test manually. 
#    t = TestShoppingApi("test_GetCategoryInfo")
#    t.test_GetCategoryInfo()
    
    unittest.main()
