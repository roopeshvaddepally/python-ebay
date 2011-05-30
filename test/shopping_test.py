from ebay.shopping import FindProducts, FindHalfProducts , GetSingleItem, GetItemStatus, GetShippingCosts, GetMultipleItems, GetUserProfile, FindPopularSearches, FindPopularItems, FindReviewsandGuides, GetCategoryInfo, GeteBayTime

#print FindProducts('JSON', 'pen', 'false', '10')
#print FindHalfProducts(encoding='JSON', query='harry', max_entries='5')
#print FindHalfProducts(encoding='JSON', product_type='ISBN', product_value='0439294827', include_selector='Items')
#print GetSingleItem(encoding='JSON', item_id='110089122715')
#print GetSingleItem(encoding='JSON', item_id='110089122716', include_selector='Description,ItemSpecifics,ShippingCosts')
#print GetItemStatus('JSON', '110089122716,110089122715')
#print GetShippingCosts('JSON', '110089122715', 'US','95128', 'true', '1')
#print GetMultipleItems('JSON', '110089122716')
#print GetUserProfile(encoding='JSON', user_id='TESTUSER_magicalbookseller')
#print GetUserProfile(encoding='JSON', user_id='TESTUSER_magicalbookseller', include_selector='Details')
#print FindPopularSearches(encoding='JSON', query='dell', category_id='58058')
#print FindPopularItems(encoding='JSON', query='potter', category_id_exclude='279')

#FindReviewsandGuides not working - Need to research later
#print FindReviewsandGuides(encoding='JSON', category_id='177')
#print FindReviewsandGuides(encoding='JSON', product_id='279')

#print GetCategoryInfo(encoding='JSON', category_id='279', include_selector='ChildCategories')
#print GeteBayTime(encoding='JSON');
