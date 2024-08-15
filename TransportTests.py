from Transport import *
from TransportManager import *


def test_transport_initialization():
    vehicle = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")
    assert vehicle.get_vehicle_id() == "Vehicle_1"
    assert vehicle.get_vehicle_type() == "Bus"
    assert vehicle.get_current_location() == (40.7, -67.4)
    assert vehicle.get_status() == "On Time"


def test_set_current_location():
    vehicle = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")
    new_location = (40.715, -74.01)
    vehicle.set_current_location(new_location)
    assert vehicle.get_current_location() == new_location


def test_set_status():
    vehicle = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")
    new_status = "Delayed"
    vehicle.set_status(new_status)
    assert vehicle.get_status() == new_status


def test_stop_initialization():
    stop = Stop("Stop_1", "Park Street", (40.7, -67.4))
    assert stop.stop_id == "Stop_1"
    assert stop.stop_name == "Park Street"
    assert stop.location == (40.7, -67.4)


def test_route_initialization():
    stops = ["Stop1", "Stop2", "Stop3"]
    route = Route("Route_1", "Route 1", stops)

    # Assertions
    assert route.route_id == "Route_1"
    assert route.name == "Route 1"
    assert len(route.stops) == 3
    assert route.stops[0] == "Stop1"
    assert len(route.vehicles) == 0


def test_add_vehicle():
    stops = ["Stop1", "Stop2", "Stop3"]
    route = Route("Route_1", "Route 1", stops)
    vehicle = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")

    route.add_vehicle(vehicle)
    assert len(route.vehicles) == 1
    assert route.vehicles[0].get_vehicle_id() == "Vehicle_1"


def test_remove_vehicle():
    stops = ["Stop1", "Stop2", "Stop3"]
    route = Route("Route_1", "Route 1", stops)
    vehicle1 = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")
    vehicle2 = Transport("Vehicle_2", "Bus", (29.2, -67.4), "Delayed")
    route.add_vehicle(vehicle1)
    route.add_vehicle(vehicle2)

    route.remove_vehicle("Vehicle_1")
    assert len(route.vehicles) == 1
    assert route.vehicles[0].get_vehicle_id() == "Vehicle_2"


def test_get_vehicles():
    stops = ["Stop1", "Stop2", "Stop3"]
    route = Route("Route_1", "Route 1", stops)
    vehicle1 = Transport("Vehicle_1", "Bus", (40.7, -67.4), "On Time")
    vehicle2 = Transport("Vehicle_2", "Bus", (29.2, -67.4), "Delayed")
    route.add_vehicle(vehicle1)
    route.add_vehicle(vehicle2)

    vehicles = route.get_vehicles()
    assert len(vehicles) == 2
    assert vehicles[0].get_vehicle_id() == "Vehicle_1"
    assert vehicles[1].get_vehicle_id() == "Vehicle_2"


def test_bus_initialization():
    bus = Bus("BuStop_1", (40.7, -67.4), "On Time")
    assert bus.get_vehicle_id() == "BuStop_1"
    assert bus.get_vehicle_type() == "Bus"
    assert bus.get_current_location() == (40.7, -67.4)
    assert bus.get_status() == "On Time"


def test_train_initialization():
    train = Train("Train1", (29.2, -67.4), "On Time")
    assert train.get_vehicle_id() == "Train1"
    assert train.get_vehicle_type() == "Train"
    assert train.get_current_location() == (29.2, -67.4)
    assert train.get_status() == "On Time"


def test_uber_initialization():
    uber = Uber("UbeRoute_1", (47.5, -67.4), "Available")
    assert uber.get_vehicle_id() == "UbeRoute_1"
    assert uber.get_vehicle_type() == "Uber"
    assert uber.get_current_location() == (47.5, -67.4)
    assert uber.get_status() == "Available"


def test_add_and_remove_route():
    transport_manager = TransportManager()
    route = Route("Route_1", "Route 1", ["Stop1", "Stop2"])
    transport_manager.add_route(route)
    assert "Route_1" in transport_manager.routes

    transport_manager.remove_route("Route_1")
    assert "Route_1" not in transport_manager.routes

    result = transport_manager.remove_route("Route_2")
    assert result == "Route ID not found"
    assert "Route_2" not in transport_manager.routes


def test_add_and_remove_vehicle():
    transport_manager = TransportManager()
    vehicle = Transport("Vehicle_1", "Bus", (0, 0), "On Time")
    transport_manager.add_vehicle(vehicle)
    assert "Vehicle_1" in transport_manager.vehicles

    transport_manager.remove_vehicle("Vehicle_1")
    assert "Vehicle_1" not in transport_manager.vehicles

    result = transport_manager.remove_vehicle("Vehicle_2")
    assert result == "Vehicle ID not found"
    assert "Vehicle_2" not in transport_manager.vehicles


def test_assign_vehicle_to_route():
    manager = TransportManager()
    route1 = Route("Route1", "First Route", [Stop("Stop_1", "Stop One", (0, 0))])
    manager.add_route(route1)
    bus = Transport("BuStop_1", "Bus", (0, 0), "On Time")
    manager.add_vehicle(bus)

    manager.assign_vehicle_to_route("BuStop_1", "Route1")
    assert bus in route1.get_vehicles()

    result = manager.assign_vehicle_to_route("Bus2", "Route1")
    assert result == "Vehicle ID not found"

    result = manager.assign_vehicle_to_route("BuStop_1", "Route2")
    assert result == "Route ID not found"


def test_update_vehicle_location():
    manager = TransportManager()
    bus = Transport("BuStop_1", "Bus", (0, 0), "On Time")
    manager.add_vehicle(bus)

    new_location = (1, 1)
    manager.update_vehicle_location("BuStop_1", new_location)
    assert bus.get_current_location() == new_location

    result = manager.update_vehicle_location("Bus2", new_location)
    assert result == "Vehicle ID not found"


def test_search_stop():
    manager = TransportManager()
    route1 = Route("Route1", "First Route", [Stop("Stop_1", "Stop One", (0, 0))])
    manager.add_route(route1)

    stop = manager.search_stop("Stop_1")
    assert stop == route1.stops[0]

    stop = manager.search_stop("Stop One")
    assert stop == route1.stops[0]

    result = manager.search_stop("Nonexistent Stop")
    assert result == "Stop not found"


def test_find_route_or_stop_by_name():
    manager = TransportManager()
    route1 = Route("Route_1", "First Route", [Stop("Stop_1", "Stop One", (0, 0))])
    manager.add_route(route1)

    found_route = manager.find_route_or_stop_by_name("First Route")
    assert found_route == route1

    found_route = manager.find_route_or_stop_by_name("first route")
    assert found_route == route1

    result = manager.find_route_or_stop_by_name("Route 67")
    assert result == "Stop or Route not found"
