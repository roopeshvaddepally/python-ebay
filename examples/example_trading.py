from ebay.trading import getCategories, filterCategories

print("All categories")
print(getCategories()) 

print("Antiques...")
for curCatXml in filterCategories(getCategories(), "Antiques"):
    print(curCatXml)
    
print("Everything with '&' character")
for curCatXml in filterCategories(getCategories(), "&"):
    print(curCatXml)