from ConfigParser import ConfigParser
import requests
from utils import relative

def GetPublicAlerts():pass
def GetUserAlerts():pass
def Login():pass
def Logout():pass

#requests method
def get_response(user_params):
    endpoint = "https://clientalerts.sandbox.ebay.com/ws/ecasvc/ClientAlerts"
    
    config = ConfigParser()
    config.read(relative("..", "config", "config.ini"))
    
    app_id = config.get("keys", "app_name")
    site_id = config.get("call", "siteid")
    version = config.get("call", "compatibility_level")

    d=dict(appid = app_id, siteid = site_id, version = version)
    
    d.update(user_params)
    
    return requests.get(endpoint, params=d)
