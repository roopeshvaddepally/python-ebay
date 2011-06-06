from os.path import join, dirname, abspath

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)

class IDTooLong(Exception): pass
class NotAValidPartner(Exception): pass

class Affliate(object):
    def __init__(customId, networkId, trackingId):
        self.customId = customId
        self.networkId = networkId
        self.trackingId = trackingId

    @property
    def customId(self):
        return self._customId
    @customId.setter
    def customId(self, customId):
        if len(customId) > 256:
            raise IDTooLong(("customId is too long. " 
                             "only upto 256 characters long"))
        self._customId = customId
    
    @property
    def networkId(self):
        return self._networkId
    @networkId.setter
    def networkId(self, networkId):
        if networkId not in list(range(2, 10)):
            raise NotAValidPartner("partner network id is between 2 to 9")
        self._networkId = networkId
    
    @property
    def trackingId(self):
        return self._trackingId
    @trackingId.setter
    def trackingId(self, trackingId):
        self._trackingId = trackingId
    
    def data(self):
        return {
            "networkId": networkId,
            "trackingId": trackingId,
            "customId" : customId,
            }

class PaginationInput(object):
    def __init__(self, entriesPerPage=100, pageNumber=1):
        self.entriesPerPage = entriesPerPage
        self.pageNumber = pageNumber
    @property
    def entriesPerPage(self):
        return self._entriesPerPage
    @entriesPerPage.setter
    def entriesPerPage(self, entriesPerPage):
        minimum_pages = 1
        maximum_pages = 100
        if minimum_pages <= entriesPerPage <= maximum_pages:
            self._entriesPerPage = entriesPerPage
        else:
            self._entriesPerPage = 100

    @property
    def pageNumber(self):
        return self._pageNumber
    @pageNumber.setter
    def pageNumber(self, pageNumber=1):
        minimum_page_number = 1
        maximum_page_number = 100
        if minimum_page_number <= pageNumber <= maximum_page_number:
            self._pageNumber = pageNumber
        else:
            self._pageNumber = 1

    def data(self):
        return {
            "pageNumber": pageNumber,
            "entriesPerPage": entriesPerPage
            }

# class SortOrder(object):
#     """Values that can be used to sort search results
# 
#     >>> s = SortOrder()
#     >>> s.data() == {"sortOrder": "BestMatch"}
#     True
#     >>> s = SortOrder("BidCountFewest")
#     >>> s.data() == {"sortOrder": "BidCountFewest", "itemFilter.name": "ListingType", "itemFilter.value": "Auction"}
#     True
#     >>> s = SortOrder("BidCountMost")
#     >>> s.data() == {"sortOrder": "BidCountMost", "itemFilter.name": "ListingType", "itemFilter.value": "Auction"}
#     True
#     >>> s = SortOrder("Distance")
#     >>> s.data() == {"sortOrder":"Distance"}
#     True
#     >>> s = SortOrder("Distance", buyerPostalCode=95112)
#     >>> s.data() == {"sortOrder":"Distance", "buyerPostalCode": "95112"}
#     True
#     
#     """
#     def __init__(self, type_="BestMatch", *args, **kwargs):
#         self.acceptable_types = ("BestMatch", "BidCountFewest", "BidCountMost",
#                             "CountryAscending", "CountryDescending",
#                             "CurrentPriceHighest", "Distance",
#                             "EndTimeSoonest", "PricePlusShippingHighest",
#                             "PricePlusShippingLowest", "StartTimeNewest")
#         self.type = type_
#         self.buyerPostalCode = kwargs.get("buyerPostalCode", None)
# 
#     @property
#     def type(self):
#         return self._type
#     @type.setter
#     def type(self, type_="BestMatch"):
#         if type_ not in self.acceptable_types:
#             type_ = "BestMatch"
#         self._type = type_
# 
#     def data(self):
#         data = {"sortOrder": self.type}
#         auction_sort_orders_types = ["BidCountFewest", "BidCountMost"]
# 
#         if self.type in auction_sort_orders_types:
#             data.update({
#                     "itemFilter.name": "ListingType",
#                     "itemFilter.value": "Auction",
#                     })
#         if self.type == "Distance" and self.buyerPostalCode is not None:
#             data.update({"buyerPostalCode": str(self.buyerPostalCode)})
# 
#         return data

class Value(object):
    def __init__(self,
                 number=None,
                 text=None,
                 url=None):
        self.number = number
        self.text = text
        self.url = url

class Specification(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []

class CompatibilityPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []

class SortOrder(object):
    def __init__(self, sortPriority):
        self.sortPriority = sortPriority
        self.subSortOrder = None

class SubSortOrder(object):
    def __init__(self, order, propertyName):
        self.order = order
        self.propertyName = propertyName

class ApplicationPropertyFilter(object):
    def __init__(self, propertyName):
        self.propertyName = propertyName
        self.values = []
