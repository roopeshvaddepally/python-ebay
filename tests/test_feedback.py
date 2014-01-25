import unittest
from lxml import etree

from ebay.feedback import *

#WARNING: YOU WILL BE PLAY`ING WITH PRODUCTION EBAY.COM, SINCE THIS API IS NOT SUPPORTED IN SANDBOX

categoryId = ["id1", "id2"]
dateRangeFrom = "date"
dateRangeTo = "date"
dateRangeEventType = "range type"
encoding = "XML"
shippingCostType = "Plane"
shippingDestinationType = "home"
shippingService = ["USPS"]
shipToCountry = ["USA", "CAN"]
transactionKey =  [{"itemId":"123", "transactionId":"72"}, {"itemId":"33", "transactionId":"21"}]


class TestFeedbackhApi(unittest.TestCase):
    def test_createDSRSummaryByCategory(self):
        result = createDSRSummaryByCategory(categoryId=categoryId,
                                            dateRangeFrom=dateRangeFrom,
                                            dateRangeTo=dateRangeTo,
                                            dateRangeEventType=dateRangeEventType,
                                            encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("ack").text
        self.assertEqual(ack, "Success")


    def test_createDSRSummaryByPeriod(self):
        result = createDSRSummaryByPeriod(dateRangeFrom=dateRangeFrom,
                                              dateRangeTo=dateRangeTo,
                                              dateRangeEventType=dateRangeEventType,
                                              encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/services}ack").text
        self.assertEqual(ack, "Success")


    def test_createDSRSummaryByShippingDetail(self):
        result = createDSRSummaryByShippingDetail(dateRangeFrom=dateRangeFrom,
                                                      dateRangeTo=dateRangeTo,
                                                      dateRangeEventType=dateRangeEventType,
                                                      shippingCostType=shippingCostType,
                                                      shippingDestinationType=shippingDestinationType,
                                                      shippingService=shippingService,
                                                      shipToCountry=shipToCountry,
                                                      encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/services}ack").text
        self.assertEqual(ack, "Success")


    def test_createDSRSummaryByTransaction(self):
        result = createDSRSummaryByTransaction(transactionKey=transactionKey, encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/services}ack").text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
