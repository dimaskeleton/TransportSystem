from Transport import *
from TransportManager import *

# Both examples being Circle Line and Kalininsko-Solntsevskaya are based off of real subway/train lines and stations
# that can be found in Moscow

# All the stops for the first line (Circle Line)
station1 = Stop("ST1", "Belorusskaya", (-30.8, -35.5))
station2 = Stop("ST2", "Krasnopresnenskaya", (-26.4, -31.6))
station3 = Stop("ST3", "Kiyevskaya", (-23.7, -26.3))
station4 = Stop("ST4", "Park Kultury", (-20.4, -24.4))
station5 = Stop("ST5", "Oktyabrskaya", (-16.1, -19.9))
station6 = Stop("ST6", "Dobryninskaya", (-14.7, -16.6))
station7 = Stop("ST7", "Paveletskaya", (-9.2, -11.3))
station8 = Stop("ST8", "Taganskaya", (-6.4, -7.2))
station9 = Stop("ST9", "Kurskaya", (-3.1, -2.9))
station10 = Stop("ST10", "Komsomolskaya", (0.5, 1.5))
station11 = Stop("ST11", "Prospekt Mira", (3.3, 4.2))
station12 = Stop("ST12", "Suvorovskaya", (7.9, 7.6))
station13 = Stop("ST13", "Novoslobodskaya", (11.5, 9.7))

# All the stations for the second train line (Kalininsko-Solntsevskaya)
station14 = Stop("ST14", "Novokosino", (63.6, 58.8))
station15 = Stop("ST15", "Novogireyevo", (59.2, 52.5))
station16 = Stop("ST16", "Perovo", (55.5, 49.7))
station17 = Stop("ST17", "Shosse Entuziastov", (52.9, 45.4))
station18 = Stop("ST18", "Aviamotornaya", (46.6, 42.5))
station19 = Stop("ST19", "Ploshchad Ilyicha", (43.4, 36.7))
station20 = Stop("ST20", "Marksistskaya", (38.1, 31.7))
station21 = Stop("ST21", "Tretyakovskaya", (32.2, 27.5))
station22 = Stop("ST22", "Volkhonka", (29.8, 24.9))
station23 = Stop("ST23", "Plyushchikha", (25.8, 21.5))
station24 = Stop("ST24", "Dorogomilovskaya", (20.4, 17.2))
station25 = Stop("ST25", "Delovoy Tsentr", (17.5, 13.6))
station26 = Stop("ST26", "Park Pobedy", (12.8, 10.2))
station27 = Stop("ST27", "Minskaya", (8.7, 6.4))
station28 = Stop("ST28", "Lomonosovsky Prospekt", (4.6, 4.3))
station29 = Stop("ST29", "Ramenki", (0.3, -82.7))
station30 = Stop("ST30", "Michurinsky Prospekt", (-2.5, 1.9))
station31 = Stop("ST31", "Ozyornaya", (-7.1, -2.7))
station32 = Stop("ST32", "Govorovo", (-11.7, -8.4))
station33 = Stop("ST33", "Solntsevo", (-15.2, -12.6))
station34 = Stop("ST34", "Borovskoye Shosse", (-18.2, -15.5))
station35 = Stop("ST35", "Novoperedelkino", (-21.7, -18.9))
station36 = Stop("ST36", "Rasskazovka", (-25.5, -21.8))
station37 = Stop("ST37", "Pykhtino", (-29.3, -24.7))
station38 = Stop("ST38", "Aeroport Vnukovo", (-34.3, -27.8))

# Adding all the stations for Circle Line
stations_circle_line = ("CircleLine", "Circle", [
    station1, station2, station3, station4, station5,
    station6, station7, station8, station9, station10,
    station11, station12, station13
])

# Stations and route for the Kalininsko-Solntsevskaya Line
stations_kalininsko_solntsevskaya = ("Kalininsko-Solntsevskaya", "Kalininsko-Solntsevskaya", [
    station14, station15, station16, station17, station18, station19, station20,
    station21, station22, station23, station24, station25, station26, station27,
    station28, station29, station30, station31, station32, station33, station34,
    station35, station36, station37, station38
])

# Transport System Manager creates instance of the TransportManager()
transport_system = TransportManager()

# Route for the Circle Line
circle_line = Route("CircleLine", "Circle Line", stations_circle_line)

# Route for the Kalininsko-Solntsevskaya Line
kalininsko_solntsevskaya_line = Route("KalininskoSolntsevskaya",
                                      "Kalininsko-Solntsevskaya", stations_kalininsko_solntsevskaya)

# Adding the new route to the system
transport_system.add_route(circle_line)
transport_system.add_route(kalininsko_solntsevskaya_line)

# Adding new trains for the Circle Line and assigning them to the route
train1 = Train("CircleLine_Train1", station1.location, "On Time")
train2 = Train("CircleLine_Train2", station4.location, "Delayed")
train3 = Train("CircleLine_Train3", station7.location, "Early")
train4 = Train("CircleLine_Train4", station10.location, "On Time")

# Adding new trains for the Kalininsko-Solntsevskaya Line
train5 = Train("KalininskoSolntsevskaya_Train1", station14.location, "On Time")
train6 = Train("KalininskoSolntsevskaya_Train2", station21.location, "Cancelled")
train7 = Train("KalininskoSolntsevskaya_Train3", station28.location, "On Time")
train8 = Train("KalininskoSolntsevskaya_Train4", station35.location, "Delayed")

# Adds the trains to the transport system to manage it
transport_system.add_vehicle(train1)
transport_system.add_vehicle(train2)
transport_system.add_vehicle(train3)
transport_system.add_vehicle(train4)

transport_system.add_vehicle(train5)
transport_system.add_vehicle(train6)
transport_system.add_vehicle(train7)
transport_system.add_vehicle(train8)

# Assigns the trains to their given routes/lines
transport_system.assign_vehicle_to_route("CircleLine_Train1", "CircleLine")
transport_system.assign_vehicle_to_route("CircleLine_Train2", "CircleLine")
transport_system.assign_vehicle_to_route("CircleLine_Train3", "CircleLine")
transport_system.assign_vehicle_to_route("CircleLine_Train4", "CircleLine")

transport_system.assign_vehicle_to_route("KalininskoSolntsevskaya_Train1", "KalininskoSolntsevskaya")
transport_system.assign_vehicle_to_route("KalininskoSolntsevskaya_Train2", "KalininskoSolntsevskaya")
transport_system.assign_vehicle_to_route("KalininskoSolntsevskaya_Train3", "KalininskoSolntsevskaya")
transport_system.assign_vehicle_to_route("KalininskoSolntsevskaya_Train4", "KalininskoSolntsevskaya")

# Displays the status of both train lines
transport_system.display_route_status("CircleLine")
transport_system.display_route_status("KalininskoSolntsevskaya")
