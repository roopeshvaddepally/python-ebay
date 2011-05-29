def configure(*args, **kwargs): pass

class EBay(object):
    """An object that helps to wrap around raw api calls.

    EBay object initializes an object which take the dev keys and
    certificates and configures the parameters being passed to the
    url calls.
    
    Instead of keys, the path to file can be given. By default, the
    object reads from the config.ini file from current working directory.
    ::
    
    >>> ebay = EBay() # reads from config.ini file.
    >>> ebay.finding.getVersion() # calls finding.py/getVersion with
                                  # appropriate parameters.
    """
    def __init__(self, dev=None, app=None, cert=None, config="config.ini"):
        ## read the config file and load the dev, app, cert variables.
        ## override the variables from the paramters passed in.
        pass
