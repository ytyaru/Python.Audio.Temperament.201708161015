#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
from abc import ABCMeta, abstractmethod

class Scales(metaclass=ABCMeta):
    @property
    @abstractmethod
    def Intervals(self): pass

