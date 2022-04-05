import requests

try:
    from  utils import get_config_store, urlopen, Request
except ImportError:
    from .utils import get_config_store, urlopen, Request

def GetPublicAlerts(ChannelID, ChannelType, EventType, MessageID=None, LastRequestTime=None, encoding="JSON"):
    user_param={'callname' : GetPublicAlerts.__name__,
    'ChannelDescriptor(0).ChannelID' : ChannelID,
    'ChannelDescriptor(0).ChannelType' : ChannelType,
    'ChannelDescriptor(0).EventType' : EventType,
    'responseencoding' : encoding}

    if MessageID:
        user_param.update({"MessageID" : MessageID})
    if LastRequestTime:
        user_param.update({"LastRequestTime" : LastRequestTime})

    response = get_response(user_param)
    return response.content

def GetUserAlerts(SessionID, SessionData, MessageID=None, encoding="JSON"):
    user_param={'callname' : GetUserAlerts.__name__,
    'SessionData' : SessionData,
    'SessionID' : SessionID,
    'responseencoding' : encoding}

    if MessageID:
        user_param.update({"MessageID" : MessageID})

    response = get_response(user_param)
    return response.content

def Login(ClientAlertsAuthToken, MessageID=None, encoding="JSON"):
    user_param={'callname' : Login.__name__,
    'ClientAlertsAuthToken' : ClientAlertsAuthToken,
    'responseencoding' : encoding}

    if MessageID:
        user_param.update({"MessageID" : MessageID})

    response = get_response(user_param)
    return response.content


def Logout(SessionID, SessionData, MessageID=None, encoding="JSON"):
    user_param={'callname' : Logout.__name__,
    'SessionData' : SessionData,
    'SessionID' : SessionID,
    'responseencoding' : encoding}

    if MessageID:
        user_param.update({"MessageID" : MessageID})

    response = get_response(user_param)
    return response.content

def get_response(user_params):
    config = get_config_store()
    app_id = config.get("keys", "app_name")
    site_id = config.get("call", "siteid")
    version = config.get("call", "compatibility_level")
    endpoint = config.get("endpoints", "client_alerts")

    d=dict(appid = app_id, siteid = site_id, version = version)
    d.update(user_params)

    return requests.get(endpoint, params=d)
