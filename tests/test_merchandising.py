import unittest
from lxml import etree

from ebay.merchandising import *

class TestMerchandisingApi(unittest.TestCase):
    def test_getDeals(self):
        result = getDeals(keywords=keywords, encoding="JSON")
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/services}ack").text
        self.assertEqual(ack, "Success")



if __name__ == '__main__':
    unittest.main()
