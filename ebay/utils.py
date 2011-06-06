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

    def data(self):
        return {
            "pageNumber": pageNumber,
            "entriesPerPage": entriesPerPage
            }

class SortOrder(object):
    def __init__(self, type_="BestMatch", *args, **kwargs):
        self.type = type_
        self.buyerPostalCode = kwargs.get("buyerPostalCode", None)

    def data(self):
        data = {"sortOrder": self.type}
        auction_sort_orders_types = ["BidCountFewest", "BidCountMost"]

        if self.type in auction_sort_orders_types:
            data.update({
                    "itemFilter.name": "ListingType",
                    "itemFilter.value": "Auction",
                    })
        if self.type == "Distance" and self.buyerPostalCode is not None:
            data.update({"buyerPostalCode": str(self.buyerPostalCode)})

        return data

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

