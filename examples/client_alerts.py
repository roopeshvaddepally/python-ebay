from ebay.client_alerts import GetPublicAlerts, GetUserAlerts, Login, Logout 

#Taken from ebay dev site, as a sample. Not actual tokens

# print GetPublicAlerts(ChannelID="370293550455", ChannelType="Item", EventType="ItemEnded", encoding="XML")
# print GetUserAlerts(SessionData="p0SVs0iK4imqkoKkI1D", SessionID="MySessionID", encoding="XML")

# print Login(ClientAlertsAuthToken="AQAAARk1obQAAA0xfDE3ODcyNHw1MjQ2fDEyMDg1NDk0Njg0ODR8anFBcGlQeVVhVENzcVJtdGk0Q0JvRGJRbTZqUHZaNmtzeXBsdXJmb3lOd3d0R0dVaGZXRGU4dnJPZi83QW1WbG1lckJ5a0toUFhYb0JQZGo2K21FVVE9PdQH6Gx9OVytZOKHinBi79BRqcEn") 

#print Logout(SessionID="AQAAARjtiKwAAA0xfDE4MXwyNTI4Mjc4OXw2MDA2fDEyMDcyNDU4MTUzNDPAcreR8zFN7kgYxffBN8IpNcfXFw", SessionData="AQAAARjtiKwAAA0xfExBQ1RWPTEyMDcxNTk0MjY1MDB8RUhXTT04NTY5Mjk4fFRJRFg9MnxMSVVQPTEyMDcxNTk0MTUyMzR8UExIUz1bMCwxMV21GsvUPVFhcxgMgs5bkosLlnW8rA")