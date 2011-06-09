from ebay.finding import getSearchKeywordsRecommendation, findItemsByKeywords, findItemsByCategory, findItemsAdvanced, findItemsByProduct, findItemsIneBayStores, getHistograms

#print getSearchKeywordsRecommendation(encoding="XML", keywords="acordian")
#print findItemsByKeywords(keywords="ipod")
#print findItemsByCategory(categoryId="123")
#print findItemsAdvanced()
#print findItemsByProduct(productId="123")
#print findItemsIneBayStores()

print getHistograms(categoryId="12")
