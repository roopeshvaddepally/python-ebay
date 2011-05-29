from ConfigParser import ConfigParser

def get_url(svc_name, operation_name):
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    app_name = config.get("keys", "app_name")
    return "/services/search/%(svc_name)s/v1?OPERATION-NAME=%(operation_name)s&SERVICE-VERSION=1.9.0&SECURITY-APPNAME=%(app_name)s&RESPONSE-DATA-FORMAT=JSON" % {
        "svc_name": svc_name,
        "operation_name": operation_name,
        "app_name": app_name
        }

def get_response(url, method="GET"):
    from httplib import HTTPConnection
    home = "svcs.sandbox.ebay.com"
    conn = HTTPConnection(home)
    conn.request(method, url)
    resp = conn.getresponse()
    response = resp.read()
    conn.close()
    return response

def configure(*args, **kwargs):
    config = ConfigParser()
    config.read("config.ini")

    dev_name = config.get("keys", "dev_name")
    app_name = config.get("keys", "app_name")
    cert_name = config.get("keys", "cert_name")
    server_url = config.get("server", "url")
    server_dir = config.get("server", "dir")
    token = config.get("auth", "token")
    siteid = config.get("call", "siteid")
    compatiblity_level = config.get("call", "compatibility_level")

    d = dict(dev_id=dev_id, app_id=app_id, cert_id=cert_id,
             server_url=server_url, server_dir=server_dir,
             token=token,siteid=siteid, 
             compatiblity_level=compatiblity_level)
    d.update(kwargs)
    return d
