# Open file
"""
Handlers
"""
from abc import ABC, abstractmethod

import logging
from logging import Logger

from ui import view, buttons

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

class CustomHandler(DefaultHandler):
    """
    Custom Handler
    """
    """
    Class
    """
    def __init__(self):
        print ('Custom Handler Init')
