# import urllib2

from lxml import etree

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request


def createDSRSummaryByCategory(categoryId , dateRangeFrom, dateRangeTo, dateRangeEventType=None, encoding="JSON"):
    root = etree.Element("createDSRSummaryByCategoryRequest", xmlns="http://www.ebay.com/marketplace/services")

    #categoryId is a List
    for cat_id in categoryId:
        categoryId_elem = etree.SubElement(root, "categoryId")
        categoryId_elem.text = cat_id

    dateRange_elem = etree.SubElement(root, "dateRange")
    dateRangeFrom_elem = etree.SubElement(dateRange_elem, "dateFrom")
    dateRangeFrom_elem.text = dateRangeFrom

    dateRangeTo_elem = etree.SubElement(dateRange_elem, "dateTo")
    dateRangeTo_elem.text = dateRangeTo

    if dateRangeEventType:
        dateRangeEventType_elem = etree.SubElement(root, "dateRangeEventType")
        dateRangeEventType_elem.text = dateRangeEventType

    request = etree.tostring(root, pretty_print=True)
    return get_response(createDSRSummaryByCategory.__name__, request, encoding)


def createDSRSummaryByPeriod(dateRangeFrom, dateRangeTo, dateRangeEventType=None, encoding="JSON"):
    root = etree.Element("createDSRSummaryByPeriodRequest", xmlns="http://www.ebay.com/marketplace/services")

    dateRange_elem = etree.SubElement(root, "dateRange")
    dateRangeFrom_elem = etree.SubElement(dateRange_elem, "dateFrom")
    dateRangeFrom_elem.text = dateRangeFrom

    dateRangeTo_elem = etree.SubElement(dateRange_elem, "dateTo")
    dateRangeTo_elem.text = dateRangeTo

    if dateRangeEventType:
        dateRangeEventType_elem = etree.SubElement(root, "dateRangeEventType")
        dateRangeEventType_elem.text = dateRangeEventType

    request = etree.tostring(root, pretty_print=True)
    return get_response(createDSRSummaryByPeriod.__name__, request, encoding)

def createDSRSummaryByShippingDetail(dateRangeFrom, dateRangeTo, dateRangeEventType=None, shippingCostType=None, shippingDestinationType=None, shippingService=None, shipToCountry=None, encoding="JSON"):
    root = etree.Element("createDSRSummaryByShippingDetailRequest", xmlns="http://www.ebay.com/marketplace/services")

    dateRange_elem = etree.SubElement(root, "dateRange")
    dateRangeFrom_elem = etree.SubElement(dateRange_elem, "dateFrom")
    dateRangeFrom_elem.text = dateRangeFrom

    dateRangeTo_elem = etree.SubElement(dateRange_elem, "dateTo")
    dateRangeTo_elem.text = dateRangeTo

    if dateRangeEventType:
        dateRangeEventType_elem = etree.SubElement(root, "dateRangeEventType")
        dateRangeEventType_elem.text = dateRangeEventType

    if shippingCostType:
        shippingCostType_elem = etree.SubElement(root, "shippingCostType")
        shippingCostType_elem.text = shippingCostType

    if shippingDestinationType:
        shippingDestinationType_elem = etree.SubElement(root, "shippingDestinationType")
        shippingDestinationType_elem.text = shippingDestinationType

    #shippingService is a List
    if shippingService and len(shippingService)>0:
        for service in shippingService:
            shippingService_elem = etree.SubElement(root, "shippingService")
            shippingService_elem.text = shippingService

    #shipToCountry is a List
    if shipToCountry:
        for country in shipToCountry:
            shipToCountry_elem = etree.SubElement(root, "shipToCountry")
            shipToCountry_elem.text = shipToCountry

    request = etree.tostring(root, pretty_print=True)
    return get_response(createDSRSummaryByShippingDetail.__name__, request, encoding)


#making transactionId required here, but it's not in the eBay API. Will fix it later
#transactionId is a list of dicts: [{itemId:123, transactionId:72}, {itemId:33, transactionId:21}]
def createDSRSummaryByTransaction(transactionKey, encoding="JSON"):
    root = etree.Element("createDSRSummaryByTransactionRequest", xmlns="http://www.ebay.com/marketplace/services")

    for t in transactionKey:
        transactionKey_elem = etree.SubElement(root, "transactionKey")

        for key in t.keys():
            itemId_elem = etree.SubElement(transactionKey_elem, key)
            itemId_elem.text =  t[key]

    request = etree.tostring(root, pretty_print=True)
    return get_response(createDSRSummaryByTransaction.__name__, request, encoding)


def getDSRSummary(jobId, encoding="JSON"):
    root = etree.Element("getDSRSummaryRequest", xmlns="http://www.ebay.com/marketplace/services")

    jobId_elem = etree.SubElement(root, "jobId")
    jobId_elem.text = jobId

    request = etree.tostring(root, pretty_print=True)
    return get_response(getDSRSummary.__name__, request, encoding)


def get_response(operation_name, data, encoding, **headers):
    config = get_config_store()
    access_token = config.get("auth", "token")
    endpoint = config.get("endpoints", "feedback")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-TOKEN": access_token,
                    "X-EBAY-SOA-RESPONSE-DATA-FORMAT": encoding}

    http_headers.update(headers)

    # req = urllib2.Request(endpoint, data, http_headers)
    req = Request(endpoint, data, http_headers)
    # res = urllib2.urlopen(req)
    res = urlopen(req)
    data = res.read()
    return data
