from ..flights_planner.Flight import Flight


class EconomyFlight(Flight):

    def __init__(self, flight_id):
        super().__init__(flight_id)

    def add_passenger(self, passenger):
        number_of_passengers = len(self.passenger_set)
        self.passenger_set.add(passenger)
        return len(self.passenger_set) == number_of_passengers + 1

    def remove_passenger(self, passenger):
        number_of_passengers = len(self.passenger_set)
        if not passenger.vip:
            self.passenger_set.remove(passenger)
        return len(self.passenger_set) == number_of_passengers - 1
