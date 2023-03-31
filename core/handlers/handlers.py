# Open file
"""
Handlers
"""
from abc import ABC, abstractmethod

import logging
from logging import Logger

from ui import views
Logger = logging.getLogger('handler_cls')


class DefaultHandler(ABC):
    """
    Default Handler
    """
    """
    Class
    """
    def __init__(self):
        print ('Default Handler Init')

    def run(self):
        raise NotImplementedError

class CustomHandler(DefaultHandler):
    """
    Custom Handler
    """
    """
    Class
    """
    def __init__(self, model=None):
        print ('Custom Handler Init')

    def run(self):
        print('Running the handler')
