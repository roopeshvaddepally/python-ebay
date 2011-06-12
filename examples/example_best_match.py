from ebay.best_match import findBestMatchItemDetailsAcrossStores, getVersion, findBestMatchItemDetailsByKeywords, findBestMatchItemDetailsAdvanced, findBestMatchItemDetailsByCategory, findBestMatchItemDetailsByProduct, findBestMatchItemDetailsBySeller, findBestMatchItemDetails

items= [{"paramName":"PriceMin", "paramValue":"50", "name":"Currency", "value":"USD"}]
print findBestMatchItemDetailsAcrossStores(keywords="ipod", siteResultsPerPage="1", itemFilter=items)

print findBestMatchItemDetailsByKeywords(keywords="ipod", siteResultsPerPage="1", itemFilter=items, ignoreFeatured="True")
print findBestMatchItemDetailsAdvanced(keywords="ipod", siteResultsPerPage="1", itemFilter=items)
print findBestMatchItemDetailsByCategory(categoryId="12", siteResultsPerPage="1", itemFilter=items)
print findBestMatchItemDetailsByProduct(productId="11", siteResultsPerPage="1")
print findBestMatchItemDetailsBySeller(categoryId="267", sellerUserName="MegaSeller")
print getVersion()

#Not working
#print findBestMatchItemDetails()
