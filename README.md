python-ebay - Python Wrapper for eBay API
========================================

Official documentation: http://developer.ebay.com/products/overview/

This wrapper intends to suport all of these operations. The list if taken from eBay Developer site.

1. Finding API:
   getSearchKeywordsRecommendation: Get recommended keywords for search  
   findItemsByKeywords: Search items by keywords  
   findItemsByCategory: Search items in a category  
   findItemsAdvanced: Advanced search capabilities  
   findItemsByProduct: Search items by a product identifier  
   findItemsIneBayStores: Search items in stores  
   getHistograms: Get category and domain meta data  

2. Shopping API:
   Item Search  
    FindProducts: Search for products on eBay via keyword or ProductID.  
    FindHalfProducts: Search for Half.com product-related information from the catalog via keywords and category based search.  

   Item Data  
    GetSingleItem: Simplified buyer specific view of item data  
    GetItemStatus: Retrieve changing item information towards the end of an auction  
    GetShippingCosts: Retrieve item shipping details  
    GetMultipleItems: Retrieve multiple item data in a single request.  

   User Reputation  
    GetUserProfile: Retrieve eBay user profile and feedback information.  

   eBay Pop!  
    FindPopularSearches: Retrieve popular and related search keywords by category or keyword.  
    FindPopularItems: Retrieve popular items by category   

   Search  
    FindReviewsandGuides: Search for reviews and guides by user, category or ProductID.  


3. Best Match API  
   findBestMatchItemDetailsAcrossStores: Returns Best Match information about items in eBay stores based on a specified set of keywords, a category ID, or both.  
   findBestMatchItemDetailsAdvanced: Returns Best Match information about items based on a specified set of keywords, a category ID, or both.  
   findBestMatchItemDetailsByCategory: Returns Best Match information about items based on a specified category ID.  
   findBestMatchItemDetailsByKeywords: Returns Best Match information about items based on a specified set of keywords.  
   findBestMatchItemDetailsByProduct: Returns Best Match information about items based on a specified product ID.  
   findBestMatchItemDetailsBySeller: Returns Best Match information about items associated with the authorized caller.  
   getBestMatchItemDetails: Returns Best Match information about items matching specified item ID values.  
   getVersion: Returns the version of the eBay Best Match Item Details server.   

4. Merchandising API  
   getDeals: Get the best deals on eBay (temporarily not functional)  
   getMostWatchedItems: Get items with the highest watch counts  
   getRelatedCategoryItems: Get items from related eBay categories  
   getSimilarItems: Get items that are similar to the specified item NEW!  
   getTopSellingProducts: Get the best selling products on eBay  


5. Feedback API  
   createDSRSummaryByCategory: Creates a seller's DSR summary report for sold items based on the categories they were listed in and a date range.  
   createDSRSummaryByPeriod: Creates a seller's DSR summary report for sold items based on a date range.  
   createDSRSummaryByShippingDetail: Creates a seller's DSR summary report for sold items based on shipping details for the items and a date range.  
   createDSRSummaryByTransaction: Creates a seller's DSR summary report for sold items specified with transaction information.  
   getDSRSummary: Retrieves a DSR report which had previously been created for specific criteria, such as a list of transactions, period of time, listing category, or shipping details.  



    
6. Trading API  
7. Large Merchant Services  
8. Product Services  
9. Client Alerts API  
10. Platform Notification API  

11. Resolution Case Management API  
    Case Retrieval Calls  
     getUserCases: Retrieve high-level information (including a case ID) of all cases for which the eBay User is involved. This includes all eBay Buyer Protection cases, Unpaid Item disputes, legacy (eBay and PayPal) disputes, and canceled transactions.  
     getEBPCaseDetail: Retrieve details of a specific eBay Buyer Protection case.  

    Seller Option Calls  
     provideTrackingInfo: Provide the tracking number and the name of the shipping carrier to the buyer.  
     issueFullRefund: Issue a full refund to the buyer.  
     offerOtherSolution: Offer the buyer an alternative solution to resolve the case.  
     escalateToCustomerSupport: Escalate an eBay Buyer Protection case to eBay customer support.  
     appealToCustomerSupport: Appeal the decision made by eBay customer support on an eBay Buyer Protection case.  

    Metadata Calls  
     getActivityOptions: Retrieve a list of the next available seller options based on the case type and the status of the case.  
     getVersion: Retrieve the current service version.  

12. Research API  
    GetPriceResearch: Returns basic pricing statistics for a keyword and date range combination.  
