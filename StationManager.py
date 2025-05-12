from typing import List
from Station import Station
from GlobalScreen import screen

'''
creating and holding all the Station instances. This is the right place to define their initial locations.
'''

class StationManager:
    def __init__(self):
        self.stations: List[Station] = []
        self.Spawn_stations()

    def Spawn_stations(self):
        # Hardcoded locations fot stations
        station_locations = [
            {"x": 200, "y": 200, "name": "Melbourne East PD"},
            {"x": 700, "y": 300, "name": "St Kilda Road PD"},
            {"x": 400, "y": 600, "name": "North Melbourne PD"},
            {"x": 1200, "y": 700, "name": "Docklands PD"} 
        ]

        # Append station data to list of stations in init
        for loc_data in station_locations:
            station = Station(loc_data["x"], loc_data["y"], loc_data["name"])
            self.stations.append(station)

    def Update(self):
        for station in self.stations:
            station.Update()

    def Draw(self):
        for station in self.stations:
            station.Draw(screen)