from ConfigParser import ConfigParser
from os.path import join, dirname, abspath

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

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)
