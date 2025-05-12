from typing import List
from Station import Station
import Globals

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

            {"x": 90, "y": 350, "name": "Far West Keilor Area"}, 
            {"x": 490, "y": 270, "name": "Keilor Park"},
            {"x": 890 , "y": 120, "name": "Broadmeadows Area"}, 
            {"x": 1150, "y": 380, "name": "Hadfield Area"}, 

            {"x": 890, "y": 610, "name": "Essendon Central"}, 
            {"x": 1410, "y": 260, "name": "Preston North/Reservoir West"},
            {"x": 1480, "y": 600, "name": "Preston Central"},

            {"x": 200, "y": 870, "name": "Sunshine Area"}, 
            {"x": 510, "y": 660, "name": "Avondale Heights Area"},
            {"x": 1095, "y": 770, "name": "Brunswick Area"},
            {"x": 1400, "y": 800, "name": "Northcote/Thornbury Area"} 
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
            station.Draw()