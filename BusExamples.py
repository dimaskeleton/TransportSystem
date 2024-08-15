from Transport import *
from TransportManager import *

# The following stops and routes are from real bus routes that can be found in Moscow

# All the bus stops defined with ID, Name, Location
stop1 = Stop("S1", "Kuryanovskiy terminal", (23.4, -100.3))
stop2 = Stop("S2", "Pr. pr. Nº 1481.", (24.7, -98.2))
stop3 = Stop("S3", "Avtobaza", (25.3, -97.3))
stop4 = Stop("S4", "Kuryanovskiy bulvar - MTsD Kuryanovo", (26.8, -96.2))
stop5 = Stop("S5", "1-y Kuryanovskiy proyezd", (27.7, -95.6))
stop6 = Stop("S6", "Batyuninskaya ulitsa", (29.3, -94.4))
stop7 = Stop("S7", "MTsD Pererva", (31.5, -93.8))
stop8 = Stop("S8", "Tekhnologicheskiy kolledzh", (31.9, -92.6))
stop9 = Stop("S9", "Nikolo-Perervinskiv monastvr", (32.6, -91.5))
stop10 = Stop("S10", "Shosseynaya ulitsa, 51", (33.1, -90.8))
stop11 = Stop("S11", "Poliklinika", (33.8, -89.3))
stop12 = Stop("S12", "Shosseynaya ulitsa, 42", (34.2, -87.6))
stop13 = Stop("S13", "Ulitsa Kukhmisterova", (34.9, -86.3))
stop14 = Stop("S14", "Shosseynaya ulitsa, 5", (35.5, -85.8))
stop15 = Stop("S15", "Metro Pechatniki", (36.0, -84.7))
stop16 = Stop("S16", "Poliklinika Nº 109", (36.6, -82.4))
stop17 = Stop("S17", "Memorial", (37.1, -81.4))
stop18 = Stop("S18", "Kinoteatr Tula", (37.7, -80.6))
stop19 = Stop("S19", "Prichal Pechatniki", (38.2, -79.3))
stop20 = Stop("S20", "Ulitsa Guryanova, 55", (38.6, -76.9))
stop21 = Stop("S21", "Ulitsa Guryanova", (39.1, -75.2))

stop22 = Stop("S22", "MTSD Pechatniki", (37.8, -74.0))
stop23 = Stop("S23", "Shosseynaya ulitsa, 1", (36.2, -73.5))
stop24 = Stop("S24", "Shosseyny proyezd", (39.9, -73.1))
stop25 = Stop("S25", "Nalogovaya inspektsiya", (40.2, -75.3))
stop26 = Stop("S26", "Metro Tekstilshchiki", (39.2, -72.8))
stop27 = Stop("S27", "Stadion", (40.4, -71.5))
stop28 = Stop("S28", "Khram", (40.6, -70.3))
stop29 = Stop("S29", "Okskaya ulitsa, 4", (41.2, -67.7))
stop30 = Stop("S30", "Magazin Optika", (41.8, -66.8))
stop31 = Stop("S31", "Okskaya ulitsa, 18", (42.2, -65.3))
stop32 = Stop("S32", "Zhigulyovskaya ulitsa, 1", (43.1, -64.6))
stop33 = Stop("S33", "Sotsialny fond Rossii", (43.9, -63.4))
stop34 = Stop("S34", "Okskaya ulitsa, 42", (44.2, -62.5))
stop35 = Stop("S35", "Metro Okskaya", (44.5, -61.9))
stop36 = Stop("S36", "Teatr Chikhachyova", (44.9, -61.2))
stop37 = Stop("S37", "Ulitsa Papernika, 17", (45.3, -60.5))
stop38 = Stop("S38", "MTSD Veshnyaki", (45.7, -59.8))

stop39 = Stop("S39", "Ilovayskaya ul.", (45.5, -59.0))
stop40 = Stop("S40", "Proyektiruyemy proyezd Nº 8201", (44.6, -58.4))
stop41 = Stop("S41", "Lyublinskiy park", (46.7, -57.6))
stop42 = Stop("S42", "Proyektiruyemy proyeza Nº 8207", (45.8, -57.1))
stop43 = Stop("S43", "Ulitsa Nizhniye Polya, 21", (46.1, -56.5))
stop44 = Stop("S44", "Torgovy tsentr", (47.0, -55.7))
stop45 = Stop("S45", "Ulitsa Nizhniye Polya", (47.4, -55.2))
stop46 = Stop("S46", "Muzykalnaya shkola imeni Glazunova", (47.2, -54.5))
stop47 = Stop("S47", "Krasnodonskaya ulitsa", (47.5, -54.0))
stop48 = Stop("S48", "43-y kvartal Maryinskogo Parka", (48.4, -53.2))
stop49 = Stop("S49", "Novorossiyskaya ulitsa", (48.9, -52.6))
stop50 = Stop("S50", "Metro Lyublino", (49.6, -51.3))
stop51 = Stop("S51", "Krasnodarskaya ulitsa, 52", (50.2, -50.9))
stop52 = Stop("S52", "Tsimlyanskaya ulitsa, 1", (50.8, -49.7))
stop53 = Stop("S53", "Tsimlyanskaya ulitsa, 2", (51.3, -49.1))
stop54 = Stop("S54", "Kolledzh Nº 26", (51.3, -48.4))
stop55 = Stop("S55", "Tsimlyanskaya ul.", (51.8, -47.6))
stop56 = Stop("S56", "Ul. Verkhn. polya, 37", (52.4, -46.3))

# All the busses in the network, each line has 4 busses and originate in different locations
bus1 = Bus("Line1_Bus1", stop1.location, "On Time")
bus2 = Bus("Line1_Bus2", stop6.location, "On Time")
bus3 = Bus("Line1_Bus3", stop11.location, "Delayed")
bus4 = Bus("Line1_Bus4", stop16.location, "Early")

bus5 = Bus("Line2_Bus1", stop22.location, "On Time")
bus6 = Bus("Line2_Bus2", stop26.location, "Delayed")
bus7 = Bus("Line2_Bus3", stop31.location, "On Time")
bus8 = Bus("Line2_Bus4", stop35.location, "On Time")

bus9 = Bus("Line3_Bus1", stop39.location, "Early")
bus10 = Bus("Line3_Bus2", stop43.location, "On Time")
bus11 = Bus("Line3_Bus3", stop47.location, "Delayed")
bus12 = Bus("Line3_Bus4", stop51.location, "Delayed")

# Route for the bus line 292
route292 = Route("Route 1", "292", [
    stop1, stop2, stop3, stop4, stop5, stop6, stop7, stop8, stop9, stop10,
    stop11, stop12, stop13, stop14, stop15, stop16, stop17, stop18, stop19,
    stop20, stop21
])

# Route for the bus line 703
route703 = Route("Route 2", "703", [
    stop1, stop2, stop3, stop4, stop5, stop6, stop7, stop8, stop9, stop10,
    stop11, stop12, stop13, stop14, stop15, stop22, stop23, stop24, stop25,
    stop26, stop27, stop28, stop29, stop30, stop31, stop32, stop33, stop34,
    stop35, stop36, stop37, stop38
])

# Route for the bus line 35
route35 = Route("Route 3", "35", [
    stop1, stop2, stop3, stop4, stop5, stop39, stop7, stop40, stop41, stop42,
    stop43, stop44, stop45, stop46, stop47, stop48, stop49, stop50, stop51,
    stop52, stop53, stop54, stop55, stop56, stop48, stop47, stop46, stop45,
    stop42, stop41, stop40, stop7, stop39, stop5, stop4, stop3, stop2, stop1
])

# Transport System Manager creates instance of the TransportManager()
transport_system = TransportManager()

# Adds the route to the transport system to keep track of it
transport_system.add_route(route292)
transport_system.add_route(route703)
transport_system.add_route(route35)

# Adds the busses to the transport system to manage it
transport_system.add_vehicle(bus1)
transport_system.add_vehicle(bus2)
transport_system.add_vehicle(bus3)
transport_system.add_vehicle(bus4)

transport_system.add_vehicle(bus5)
transport_system.add_vehicle(bus6)
transport_system.add_vehicle(bus7)
transport_system.add_vehicle(bus8)

transport_system.add_vehicle(bus9)
transport_system.add_vehicle(bus10)
transport_system.add_vehicle(bus11)
transport_system.add_vehicle(bus12)

# Assigns the busses to the routes
transport_system.assign_vehicle_to_route("Line1_Bus1", "Route 1")
transport_system.assign_vehicle_to_route("Line1_Bus2", "Route 1")
transport_system.assign_vehicle_to_route("Line1_Bus3", "Route 1")
transport_system.assign_vehicle_to_route("Line1_Bus4", "Route 1")

transport_system.assign_vehicle_to_route("Line2_Bus1", "Route 2")
transport_system.assign_vehicle_to_route("Line2_Bus2", "Route 2")
transport_system.assign_vehicle_to_route("Line2_Bus3", "Route 2")
transport_system.assign_vehicle_to_route("Line2_Bus4", "Route 2")

transport_system.assign_vehicle_to_route("Line3_Bus1", "Route 3")
transport_system.assign_vehicle_to_route("Line3_Bus2", "Route 3")
transport_system.assign_vehicle_to_route("Line3_Bus3", "Route 3")
transport_system.assign_vehicle_to_route("Line3_Bus4", "Route 3")

# Displays the route status for each line
transport_system.display_route_status("Route 1")
transport_system.display_route_status("Route 2")
transport_system.display_route_status("Route 3")
