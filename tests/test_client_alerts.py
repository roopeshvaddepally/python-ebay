import unittest
from lxml import etree

from ebay.client_alerts import *

ChannelID = "123"
ChannelType = "Type"
EventType = "Type"
MessageID = "mid"
LastRequestTime = "time"
encoding = "XML"
SessionID = "sid"
SessionData = "sdata"
ClientAlertsAuthToken = "token here"

class TestClientAlertsApi(unittest.TestCase):
    def test_GetPublicAlerts(self):
        result = GetPublicAlerts(ChannelID=ChannelID, \
                                 ChannelType=ChannelType, \
                                 EventType=EventType, MessageID=MessageID, \
                                 LastRequestTime=LastRequestTime, \
                                 encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_GetUserAlerts(self):
        result = GetUserAlerts(SessionID=SessionID, \
                               SessionData=SessionData, \
                               MessageID=MessageID, \
                               encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_Login(self):
        result = Login(ClientAlertsAuthToken=ClientAlertsAuthToken, \
                       MessageID=MessageID, \
                       encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


    def test_Logout(self):
        result = Logout(SessionID=SessionID, \
                        SessionData=SessionData, \
                        MessageID=MessageID, \
                        encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{http://www.ebay.com/marketplace/search/v1/services}ack").text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
