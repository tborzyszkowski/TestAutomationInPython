from abc import ABC, abstractmethod

VIP_FACTOR = 10
USUAL_FACTOR = 20


class Mileage(ABC):

    def __init__(self):
        self.passengers_mileage = {}
        self.passengers_points = {}

    def add_mileage(self, passenger, miles):
        if passenger in self.passengers_mileage:
            self.passengers_mileage[passenger] += int(miles)
        else:
            self.passengers_mileage[passenger] = int(miles)

    def calculate_given_points(self):
        for passenger in self.passengers_mileage:
            if passenger.vip:
                self.passengers_points[passenger] = self.passengers_mileage[passenger] / VIP_FACTOR
            else:
                self.passengers_points[passenger] = self.passengers_mileage[passenger] / USUAL_FACTOR