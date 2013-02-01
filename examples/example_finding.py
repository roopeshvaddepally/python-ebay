from ebay.finding import (getSearchKeywordsRecommendation, findItemsByKeywords, 
                          findItemsByCategory, findItemsAdvanced, 
                          findItemsByProduct, findItemsIneBayStores, 
                          getHistograms)
from ebay.utils import set_config_file

#set_config_file("../config.ini")

print getSearchKeywordsRecommendation(encoding="XML", keywords="acordian")
print findItemsByKeywords(keywords="ipod", encoding="XML", 
                          paginationInput = {"entriesPerPage": "5", 
                                             "pageNumber"    : "1"})
print findItemsByCategory(categoryId="123")
print findItemsAdvanced()
print findItemsByProduct(productId="123")
print findItemsIneBayStores()
print getHistograms(categoryId="12")
