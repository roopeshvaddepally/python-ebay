from ebay.merchandising import getDeals, getMostWatchedItems, getRelatedCategoryItems, getSimilarItems, getTopSellingProducts 


print getDeals(encoding="XML", keywords="ipod") #This operation is not documented
print getMostWatchedItems(encoding="JSON") 
print getRelatedCategoryItems(encoding="XML", categoryId="12") 
print getSimilarItems(encoding="XML", itemId="73")
print getTopSellingProducts(encoding="JSON") 
