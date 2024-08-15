"""
Contract: Manage and organize a transportation network such as routes and vehicles
Purpose:
    - Allow for adding, removing, changing routes and vehicles
    - Allow vehicles to be assigned to routes
    - Update vehicle location
    - Search for stops or routes by name or ID
"""


class TransportManager:
    # Initializes storage for routes and vehicles within the transportation network
    def __init__(self):
        self.routes = {}  # Stores all the routes in the transportation system
        self.vehicles = {}  # Stores all the vehicles in the transportation system

    # Adds a route to the transportation system based on it's ID
    def add_route(self, route):
        self.routes[route.route_id] = route  # Adds the given route object to the route dictionary

    # Removes a route from the transportation system based on it's ID
    def remove_route(self, route_id):
        if route_id in self.routes:
            del self.routes[route_id]  # Removes the route with the specified ID from the route dictionary
        else:
            return "Route ID not found"  # Prints an error in case a problem occurs removing a route

    # Adds a vehicle to the transportation system with its ID
    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.get_vehicle_id()] = vehicle  # Adds the given vehicle to the vehicles dictionary

    # Removes a vehicle from the system based on it's ID
    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]  # Removes the vehicle with the specified ID from the vehicles dictionary
        else:
            return "Vehicle ID not found"  # Prints an error message if the vehicle ID is not found

    # Assigns a vehicle to the given route
    def assign_vehicle_to_route(self, vehicle_id, route_id):
        if vehicle_id not in self.vehicles:
            return "Vehicle ID not found"  # Prints an error message if the vehicle ID is not found

        if route_id not in self.routes:
            return "Route ID not found"  # Prints an error message if the route ID is not found

        # Adds the vehicle to the specified route based on the ID
        self.routes[route_id].add_vehicle(self.vehicles[vehicle_id])

    # Updates the location of the given vehicle
    def update_vehicle_location(self, vehicle_id, new_location):
        if vehicle_id in self.vehicles:
            # Updates the given vehicle's location by its ID
            self.vehicles[vehicle_id].set_current_location(new_location)
        else:
            return "Vehicle ID not found"  # Prints an error message if the vehicle ID is not found

    # Search for a stop by its name or ID regardless of route
    def search_stop(self, stop_name_or_id):
        # Iterate over all routes and their stops to find a matching stop
        for route_id, route in self.routes.items():
            for stop in route.stops:
                # looks for name or ID of the stop to search for
                if stop.stop_id == stop_name_or_id or stop.stop_name == stop_name_or_id:
                    return stop  # Returns the Stop searched if a match is found
        return "Stop not found"  # Returns an error if a stop wasn't found

    # Searches for a route by its name
    # Returns the route if it's found
    def find_route_or_stop_by_name(self, name):
        # Iterates through all the routes
        for route_id, route in self.routes.items():
            # Check if the route name matches the search criteria
            if route.name.lower() == name.lower():
                return route  # Return the Route if a match is found (case insensitive)
        return "Stop or Route not found"

    # Displays the status of the given route with ID, Location, and Status
    def display_route_status(self, route_id):
        if route_id in self.routes:  # Check if the route ID is in the route dictionary
            route = self.routes[route_id]  # Gets the route
            print(f"Route: {route.name}")  # Prints the name of the route
            for vehicle in route.get_vehicles():  # Iterates through each vehicle on the route
                # Return details of each vehicle, including ID, current location, and status.
                print(f"Vehicle ID: {vehicle.get_vehicle_id()}, Location: {vehicle.get_current_location()}, "
                      f"Status: {vehicle.get_status()}")
        else:
            return "Route ID not found"
