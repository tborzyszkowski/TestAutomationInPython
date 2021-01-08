from abc import ABC, abstractmethod


class Passenger(ABC):

    def __init__(self, name, vip):
        self.__name = name
        self.__vip = vip

    @property
    def name(self):
        return self.__name

    @property
    def vip(self):
        return self.__vip
