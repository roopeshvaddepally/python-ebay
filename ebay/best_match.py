import urllib2
from ConfigParser import ConfigParser
from utils import relative

def findBestMatchItemDetailsAcrossStores():
     request = """<?xml version="1.0" encoding="utf-8"?>
     <findBestMatchItemDetailsAcrossStoresRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
     <siteResultsPerPage>50</siteResultsPerPage>
     <entriesPerPage>50</entriesPerPage>
     <ignoreFeatured>true</ignoreFeatured>
     <keywords>ipod</keywords>
     <itemFilter>
     <paramName>PriceMin</paramName>
     <paramValue>50</paramValue>
     <name>Currency</name>
     <value>USD</value>
     </itemFilter>
     <itemFilter>
     <paramName>PriceMax</paramName>
     <paramValue>100</paramValue>
     </itemFilter>
     </findBestMatchItemDetailsAcrossStoresRequest>"""
     return get_response(findBestMatchItemDetailsAcrossStores.__name__, request)

    
def findBestMatchItemDetailsAdvanced():
    request = """<?xml version="1.0" encoding="utf-8"?>
<findBestMatchItemDetailsAdvancedRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <keywords>ipod</keywords>
  <categoryId>12</categoryId>
  <siteResultsPerPage>50</siteResultsPerPage>
  <entriesPerPage>50</entriesPerPage>
  <outputSelector>SellerInfo</outputSelector>
  <outputSelector>FirstPageSummary</outputSelector>
  <ignoreFeatured>true</ignoreFeatured>
  <postSearchSellerFilter>
    <sellerUserName>MegaSeller</sellerUserName>
  </postSearchSellerFilter> 
</findBestMatchItemDetailsAdvancedRequest>"""
    
    return get_response(findBestMatchItemDetailsAdvanced.__name__, request)
    
def findBestMatchItemDetailsByCategory():
    request = """<?xml version="1.0" encoding="utf-8"?>
<findBestMatchItemDetailsByCategoryRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <siteResultsPerPage>200</siteResultsPerPage>
  <entriesPerPage>200</entriesPerPage>
  <categoryId>267</categoryId>
  <outputSelector>FirstPageSummary</outputSelector>
  <postSearchItemFilter>
    <itemId>170002453234</itemId>
    <itemId>170002453412</itemId>
  </postSearchItemFilter>
</findBestMatchItemDetailsByCategoryRequest>"""

    return get_response(findBestMatchItemDetailsByCategory.__name__, request) 

def findBestMatchItemDetailsByKeywords():
    request = """<?xml version="1.0" encoding="utf-8"?>
    <findBestMatchItemDetailsByKeywordsRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <keywords>ipod</keywords>
  <siteResultsPerPage>50</siteResultsPerPage>
  <entriesPerPage>50</entriesPerPage>
  <ignoreFeatured>true</ignoreFeatured>
  <outputSelector>FirstPageSummary</outputSelector>
  <outputSelector>SellerInfo</outputSelector>
  <itemFilter>
    <name>Condition</name>
    <value>Used</value>
  </itemFilter>
  <itemFilter>
    <name>ListingType</name>
    <value>AuctionWithBIN</value>
  </itemFilter></findBestMatchItemDetailsByKeywordsRequest>"""

    return get_response(findBestMatchItemDetailsByKeywords.__name__, request)
    
def findBestMatchItemDetailsByProduct():
    request = """<?xml version="1.0" encoding="utf-8"?>
<findBestMatchItemDetailsByProductRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <productId type="ReferenceID">8562593</productId>
  <siteResultsPerPage>50</siteResultsPerPage>
  <outputSelector>SellerInfo</outputSelector>
</findBestMatchItemDetailsByProductRequest>"""

    return get_response(findBestMatchItemDetailsByProduct.__name__, request)
    
def findBestMatchItemDetailsBySeller():
    request = """<?xml version="1.0" encoding="utf-8"?>
<findBestMatchItemDetailsBySellerRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <sellerUserName>MegaSeller</sellerUserName>
  <categoryId>267</categoryId>
</findBestMatchItemDetailsBySellerRequest>"""

    return get_response(findBestMatchItemDetailsBySeller.__name__, request)

#Not working
def findBestMatchItemDetails():
    request = """<?xml version="1.0" encoding="utf-8"?>
<getBestMatchItemDetailsRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <itemId>13474073440</itemId>
  <itemId>23484479761</itemId>
</getBestMatchItemDetailsRequest>"""

    return get_response(findBestMatchItemDetails.__name__,request)
    
def getVersion():
    request="""<?xml version="1.0" encoding="utf-8"?>
<getVersionRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
</getVersionRequest>"""

    return get_response(getVersion.__name__, request)

def get_response(operation_name, data):
    endpoint='https://svcs.ebay.com/services/search/BestMatchItemDetailsService/v1'
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    access_token = config.get("auth", "token")

    http_headers = {"X-EBAY-SOA-OPERATION-NAME": operation_name,
                    "X-EBAY-SOA-SECURITY-TOKEN": access_token}
    
    req = urllib2.Request(endpoint, data, http_headers)
    res = urllib2.urlopen(req)
    data = res.read()
    return data
