from behave import *
from src.bdd.flights_planner.EconomyFlight import EconomyFlight
from src.bdd.flights_planner.BusinessFlight import BusinessFlight
from src.bdd.flights_planner.PremiumFlight import PremiumFlight
from src.bdd.flights_planner.Passenger import Passenger


use_step_matcher("re")


@given("there is an economy flight")
def step_impl(context):
    context.economy_flight = EconomyFlight("1")


@when("we have a usual passenger")
def step_impl(context):
    context.mike = Passenger("Mike", False)


@then("you can add and remove him from an economy flight")
def step_impl(context):
    assert context.economy_flight.flight_id == "1"
    assert context.economy_flight.add_passenger(context.mike)
    assert len(context.economy_flight.passenger_set) == 1
    assert [el for el in context.economy_flight.passenger_set][0].name == "Mike"
    assert context.economy_flight.remove_passenger(context.mike)
    assert len(context.economy_flight.passenger_set) == 0


@when("we have a VIP passenger")
def step_impl(context):
    context.john = Passenger("John", True)


@then("you can add him but cannot remove him from an economy flight")
def step_impl(context):
    assert context.economy_flight.flight_id == "1"
    assert context.economy_flight.add_passenger(context.john)
    assert len(context.economy_flight.passenger_set) == 1
    assert context.john.name == "John"
    assert not context.economy_flight.remove_passenger(context.john)
    assert len(context.economy_flight.passenger_set) == 1


@given("there is an business flight")
def step_impl(context):
    context.business_flight = BusinessFlight("2")


@then("you cannot add or remove him from a business flight")
def step_impl(context):
    assert context.business_flight.flight_id == "2"
    assert not context.business_flight.add_passenger(context.mike)
    assert len(context.business_flight.passenger_set) == 0
    assert not context.business_flight.remove_passenger(context.mike)
    assert len(context.business_flight.passenger_set) == 0


@then("you can add him but cannot remove him from a business flight")
def step_impl(context):
    assert context.business_flight.flight_id == "2"
    assert context.business_flight.add_passenger(context.john)
    assert len(context.business_flight.passenger_set) == 1
    assert not context.business_flight.remove_passenger(context.john)
    assert len(context.business_flight.passenger_set) == 1


@step("you cannot add a usual passenger to an economy flight more than once")
def step_impl(context):
    for i in range(10):
        context.economy_flight.add_passenger(context.mike)

    assert len(context.economy_flight.passenger_set) == 1
    assert context.mike in context.economy_flight.passenger_set
    assert [el for el in context.economy_flight.passenger_set][0].name == "Mike"


@step("you cannot add a VIP passenger to an economy flight more than once")
def step_impl(context):
    for i in range(10):
        context.economy_flight.add_passenger(context.john)

    assert len(context.economy_flight.passenger_set) == 1
    assert context.john in context.economy_flight.passenger_set
    assert [el for el in context.economy_flight.passenger_set][0].name == "John"


@step("you cannot add a VIP passenger to a business flight more than once")
def step_impl(context):
    for i in range(10):
        context.business_flight.add_passenger(context.john)

    assert len(context.business_flight.passenger_set) == 1
    assert context.john in context.business_flight.passenger_set
    assert [el for el in context.business_flight.passenger_set][0].name == "John"


@given("there is an premium flight")
def step_impl(context):
    context.premium_flight = PremiumFlight("3")


@then("you cannot add or remove him from a premium flight")
def step_impl(context):
    assert not context.premium_flight.add_passenger(context.mike)
    assert len(context.premium_flight.passenger_set) == 0
    assert not context.premium_flight.remove_passenger(context.mike)
    assert len(context.premium_flight.passenger_set) == 0


@then("you can add and remove him from a premium flight")
def step_impl(context):
    assert context.premium_flight.add_passenger(context.john)
    assert len(context.premium_flight.passenger_set) == 1
    assert context.premium_flight.remove_passenger(context.john)
    assert len(context.premium_flight.passenger_set) == 0


@step("you cannot add a VIP passenger to a premium flight more than once")
def step_impl(context):
    for i in range(10):
        context.premium_flight.add_passenger(context.john)

    assert len(context.premium_flight.passenger_set) == 1
    assert context.john in context.premium_flight.passenger_set
    assert [el for el in context.premium_flight.passenger_set][0].name == "John"
