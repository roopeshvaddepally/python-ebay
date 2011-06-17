import unittest
from lxml import objectify

from ebay.resolution_case_management import *


caseStatusFilter = ["OPEN","CLOSED"]
caseTypeFilter =  ["EBP_INR","RETURN"]
creationDateRangeFilterFrom = "2011-01-01T19:09:02.768Z"
creationDateRangeFilterTo = "2011-04-01T19:09:02.768Z"
itemFilter = {"itemId":"123", "transactionId":"72"}
paginationInput = {"entriesPerPage":"5", "pageNumber":"10"}
sortOrder = "CASE_STATUS_ASCENDING"

caseId = "1"
caseType = "2"
carrierUsed = "US"
trackingNumber = "3"
comments = "MyComment"

messageToBuyer = "Hello Buyer"
escalationReason = {"sellerSNADReason" : "BUYER_STILL_UNHAPPY_AFTER_REFUND"}
appealReason = "Buyer is dumb!"

encoding = "XML"


class TestResolutionCaseManagementApi(unittest.TestCase):
    def test_getUserCases(self):
        result = getUserCases(caseStatusFilter = caseStatusFilter,
                              caseTypeFilter = caseTypeFilter,
                              creationDateRangeFilterFrom = creationDateRangeFilterFrom,
                              creationDateRangeFilterTo = creationDateRangeFilterTo,
                              itemFilter = itemFilter,
                              paginationInput = paginationInput,
                              sortOrder = sortOrder,
                              encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Warning")

    def test_getEBPCaseDetail(self):
        result = getEBPCaseDetail(caseId=caseId, caseType=caseType, encoding=encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_provideTrackingInfo(self):
        result = provideTrackingInfo(caseId = caseId,
                                         caseType = caseType,
                                         carrierUsed = carrierUsed,
                                         trackingNumber = trackingNumber,
                                         comments = comments,
                                         encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_issueFullRefund(self):
        result = issueFullRefund(caseId = caseId,
                                     caseType = caseType,
                                     comments = comments,
                                     encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_offerOtherSolution(self):
        result = offerOtherSolution(caseId = caseId,
                                        caseType = caseType,
                                        messageToBuyer = messageToBuyer,
                                        encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_escalateToCustomerSuppport(self):
        result = escalateToCustomerSuppport(caseId = caseId,
                                            caseType = caseType,
                                            escalationReason = escalationReason,
                                            comments = comments,
                                            encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Warning")

    def test_appealToCustomerSupport(self):
        result = appealToCustomerSupport(caseId = caseId,
                                             caseType = caseType,
                                             appealReason = appealReason,
                                             comments = comments,
                                             encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_getActivityOptions(self):
        result = getActivityOptions(caseId = caseId,
                                        caseType = caseType,
                                        encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Failure")

    def test_getVersion(self):
        result = getVersion(encoding = encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()
