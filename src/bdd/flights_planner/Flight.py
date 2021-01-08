from abc import ABC, abstractmethod


class Flight(ABC):

    def __init__(self, flight_id):
        self.__flight_id = flight_id
        self.__passenger_set = set()

    @property
    def flight_id(self):
        return self.__flight_id

    @property
    def passenger_set(self):
        return self.__passenger_set

    @passenger_set.setter
    def passenger_set(self, value):
        self.__passenger_set = value

    @abstractmethod
    def add_passenger(self, passenger):
        pass

    @abstractmethod
    def remove_passenger(self, passenger):
        pass
