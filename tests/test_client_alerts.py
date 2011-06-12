import unittest
from lxml import etree

from ebay.client_alerts import *

ChannelID = "370293550455"
ChannelType = "Item"
EventType = "ItemEnded"
MessageID = "1"
LastRequestTime = "2006-12-12T08:00:00"
encoding = "XML"
SessionID = "MySessionID"
SessionData = "p0SVs0iK4imqkoKkI1D"
ClientAlertsAuthToken = "AQAAARk1obQAAA0xfDE3ODcyNHw1MjQ2fDEyMDg1NDk0Njg0ODR8anFBcGlQeVVhVENzcVJtdGk0Q0JvRGJRbTZqUHZaNmtzeXBsdXJmb3lOd3d0R0dVaGZXRGU4dnJPZi83QW1WbG1lckJ5a0toUFhYb0JQZGo2K21FVVE9PdQH6Gx9OVytZOKHinBi79BRqcEn"


class TestClientAlertsApi(unittest.TestCase):
    def test_GetPublicAlerts(self):
        result = GetPublicAlerts(ChannelID=ChannelID, \
                                 ChannelType=ChannelType, \
                                 EventType=EventType, MessageID=MessageID, \
                                 LastRequestTime=LastRequestTime, \
                                 encoding=encoding)
        root = etree.fromstring(result)
        print root[0]
        ack = root.find("{urn:ebay:apis:eBLBaseComponents}Ack").text
        self.assertEqual(ack, "Success")


    def test_GetUserAlerts(self):
        result = GetUserAlerts(SessionID=SessionID, \
                               SessionData=SessionData, \
                               MessageID=MessageID, \
                               encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{urn:ebay:apis:eBLBaseComponents}Ack").text
        self.assertEqual(ack, "Failure")

    #Not sure how to fix it, the return value when request failing is:  issue#5
    def test_Login(self):
        result = Login(ClientAlertsAuthToken=ClientAlertsAuthToken, \
                       MessageID=MessageID, \
                       encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{urn:ebay:apis:eBLBaseComponents}Ack").text
        self.assertEqual(ack, "Failure")


    def test_Logout(self):
        result = Logout(SessionID=SessionID, \
                        SessionData=SessionData, \
                        MessageID=MessageID, \
                        encoding=encoding)
        root = etree.fromstring(result)
        ack = root.find("{urn:ebay:apis:eBLBaseComponents}Ack").text
        self.assertEqual(ack, "Failure")


if __name__ == '__main__':
    unittest.main()
