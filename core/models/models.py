# Template file
"""
Models
"""
import os
from abc import ABC, abstractmethod

class ModelAbstract(ABC):
    """
    Model
    """
    def __iter__(self):
        """

        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, item):
        """
        Returns an object with a .items() call method
        that iterates over key,value pairs of its information.
        :param item:
        :return:
        """
        raise NotImplementedError

    @property
    def item_type(self):
        """

        :return:
        """
        raise NotImplementedError

class ElementModel(ModelAbstract):
    """
    ElementModel
    """
    item_type = "element"

    def __init__(self, elements=None):
        """

        :param elements:
        """
        if elements is None:
            elements = {}
        self.elements = elements

    def __iter__(self):
        """

        :return:
        """
        yield self.elements

    def add(self, element):
        """
        Appends an element to elements
        :param element:
        :return:
        """
        self.elements[element.name] = element

    def remove(self, element_name):
        """
        Pops an element from elements
        :param element_name:
        :return:
        """
        self.elements.pop(element_name)

    def get(self, element):
        """
        Get a particular script from a list of default_source
        :param script: (ScriptAbstract)
        :return: script (ScriptAbstract) or Does not exist Error
        """
        try:
            return self.elements[element]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")
