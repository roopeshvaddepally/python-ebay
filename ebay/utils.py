from os.path import join, dirname, abspath

def relative(*paths):
    return join(dirname(abspath(__file__)), *paths)
