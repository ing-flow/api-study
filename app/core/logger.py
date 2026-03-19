import logging

def get_app_logger(name: str = __name__):
    return logging.getLogger(name)

def get_access_logger():
    return logging.getLogger("access")