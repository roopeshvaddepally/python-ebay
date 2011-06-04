from ebay.resolution_case_management import getUserCases, getEBPCaseDetail, provideTrackingInfo, issueFullRefund, offerOtherSolution, escalateToCustomerSuppport, appealToCustomerSupport, getActivityOptions, getVersion 

#DO NOT HAVE A CASE ID ON SANDBOX, NEED TO GENERATE AND CHECK ALL OPERATIONS

# case retrieval calls
print getUserCases() 
print getEBPCaseDetail() 

# Seller Option Calls
print provideTrackingInfo() 
print issueFullRefund() 
print offerOtherSolution() 
print escalateToCustomerSuppport() 
print appealToCustomerSupport() 

# Metadata calls
print getActivityOptions()
print getVersion()
