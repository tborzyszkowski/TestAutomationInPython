from behave import *
from src.bdd.flights_planner.Passenger import Passenger
from src.bdd.flights_planner.Mileage import Mileage

use_step_matcher("re")


@given("we have a usual passenger with a mileage")
def step_impl(context):
    context.mike = Passenger("Mike", False)
    context.mileage = Mileage()


@when("the usual passenger travels (?P<mileage1>.+) and (?P<mileage2>.+) and (?P<mileage3>.+)")
def step_impl(context, mileage1, mileage2, mileage3):
    context.mileage.add_mileage(context.mike, mileage1)
    context.mileage.add_mileage(context.mike, mileage2)
    context.mileage.add_mileage(context.mike, mileage3)


@then("the bonus points of the usual passenger should be (?P<points>.+)")
def step_impl(context, points):
    context.mileage.calculate_given_points()
    assert int(points) == int(context.mileage.passengers_points[context.mike])


@given("we have a VIP passenger with a mileage")
def step_impl(context):
    context.john = Passenger("John", True)
    context.mileage = Mileage()


@when("the VIP passenger travels (?P<mileage1>.+) and (?P<mileage2>.+) and (?P<mileage3>.+)")
def step_impl(context, mileage1, mileage2, mileage3):
    context.mileage.add_mileage(context.john, mileage1)
    context.mileage.add_mileage(context.john, mileage2)
    context.mileage.add_mileage(context.john, mileage3)


@then("the bonus points of the VIP passenger should be (?P<points>.+)")
def step_impl(context, points):
    context.mileage.calculate_given_points()
    assert int(points) == int(context.mileage.passengers_points[context.john])
