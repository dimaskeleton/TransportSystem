from Transport import *
from TransportManager import *

# Just came up with generic places for example to use as Uber/Taxi pickup stops

uber_pickup1 = Stop("Pickup1", "Downtown", (27.3, 38.7))
uber_pickup2 = Stop("Pickup2", "Mall", (-10.2, -21.5))
uber_pickup3 = Stop("Pickup3", "Seton Hall University", (22.2, -29.8))
uber_pickup4 = Stop("Pickup4", "JFK Airport", (50.4, 76.9))
uber_pickup5 = Stop("Pickup5", "OMGyro", (22.2, -33.6))

# Creates instances of the ubers with location
uber1 = Uber("Uber1", uber_pickup1.location, "Available")
uber2 = Uber("Uber2", uber_pickup2.location, "Not Available")
uber3 = Uber("Uber3", uber_pickup3.location, "Available")
uber4 = Uber("Uber4", uber_pickup4.location, "Available")
uber5 = Uber("Uber5", uber_pickup5.location, "Cancelled")

# Transport System Manager creates instance of the TransportManager()
transport_system = TransportManager()

# Adds the uber vehicle to the transport system to keep track of it
transport_system.add_vehicle(uber1)
transport_system.add_vehicle(uber2)
transport_system.add_vehicle(uber3)
transport_system.add_vehicle(uber4)
transport_system.add_vehicle(uber5)

# Creates routes for the Ubers based on the location
uber_route_downtown = Route("UberRoute_Downtown", "Downtown", [uber_pickup1])
uber_route_mall = Route("UberRoute_Mall", "Mall", [uber_pickup2])
uber_route_university = Route("UberRoute_University", "University", [uber_pickup3])
uber_route_airport = Route("UberRoute_Airport", "Airport", [uber_pickup4])
uber_route_OMGyro = Route("UberRoute_OMGyro", "OMGyro", [uber_pickup5])

# Adds the uber route to the transport system to keep track of it
transport_system.add_route(uber_route_downtown)
transport_system.add_route(uber_route_mall)
transport_system.add_route(uber_route_university)
transport_system.add_route(uber_route_airport)
transport_system.add_route(uber_route_OMGyro)

# Assigns uber to their given route
transport_system.assign_vehicle_to_route("Uber1", "UberRoute_Downtown")
transport_system.assign_vehicle_to_route("Uber2", "UberRoute_Mall")
transport_system.assign_vehicle_to_route("Uber3", "UberRoute_University")
transport_system.assign_vehicle_to_route("Uber4", "UberRoute_Airport")
transport_system.assign_vehicle_to_route("Uber5", "UberRoute_OMGyro")

# Displays the status of all the Uber's in the system
transport_system.display_route_status("UberRoute_Downtown")
transport_system.display_route_status("UberRoute_Mall")
transport_system.display_route_status("UberRoute_University")
transport_system.display_route_status("UberRoute_Airport")
transport_system.display_route_status("UberRoute_OMGyro")
