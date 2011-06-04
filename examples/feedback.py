from ebay.feedback import createDSRSummaryByCategory, createDSRSummaryByPeriod, createDSRSummaryByShippingDetail, createDSRSummaryByTransaction, getDSRSummary

transactionId= [{"itemId":"123", "transactionId":"72"}, {"itemId":"33", "transactionId":"21"}]

#WARNING: YOU WILL BE PLAYING WITH PRODUCTION EBAY.COM, SINCE THIS API IS NOT SUPPORTED IN SANDBOX
#print createDSRSummaryByCategory("12", "2011-04-30T09:00:00", "2011-05-30T09:00:00")
#print createDSRSummaryByPeriod("2011-04-30T09:00:00", "2011-05-30T09:00:00")
#print createDSRSummaryByShippingDetail("2011-04-30T09:00:00", "2011-05-30T09:00:00")
#print createDSRSummaryByTransaction(transactionId)
print getDSRSummary("1")
