from utils import get_url, get_response

def url(operation_name): return get_url("FindingService", operation_name)

def getSearchKeywordsRecommendation(keywords):
    if not keywords: print "enter a keyword"
    response = get_response("%(url)s&keywords=%(kw)s" % {
            "url" : url("getSearchKeywordsRecommendation"),
            "kw" : keywords,
            })
    return response
    
def findItemsByKeywords(): pass
def findItemsByCategory(): pass
def findItemsAdvanced(): pass
def findItemsByProduct(): pass
def findItemsIneBayStores(): pass
def getHistograms(): pass
