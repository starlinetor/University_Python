from math import sqrt

def read_drones() -> list[list[str]]:
    #open drone file
    drone_file : TextIOWrapper = open("drones.txt", "r", encoding="utf-8")
    drone_data : list[list[str]] = []
    for line in drone_file:
        
        if line == "":
            continue
        
        #save each line
        first_division = line.removesuffix("\n").split(":")
        drone_data.append([first_division[0]] + first_division[1].split(",")) 
    #close students file
    drone_file.close()
    return drone_data

def read_coordinate() -> list[list[str]]:
    #open coordinate file
    coordinate_file : TextIOWrapper = open("coordinate.txt", "r", encoding="utf-8")
    coordinate_data : list[list[str]] = []
    for line in coordinate_file:
        
        if line == "":
            continue
        
        #save each line
        first_division = line.removesuffix("\n").split(":")
        coordinate_data.append([first_division[0]] + first_division[1].split(",")) 
    #close students file
    coordinate_file.close()
    return coordinate_data

def distance(stations : list[list[str]], station_id_1 : str, station_id_2:str) -> float:
    for station in stations:
        if station[0] == station_id_1:
            x1 = float(station[1])
            y1 = float(station[2])
        elif station[0] == station_id_2:
            x2 = float(station[1])
            y2 = float(station[2])
    
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def find_most_in_need_drone(drones : list[list[str]], coordinate : list[list[str]]) -> float:
    drone_data : list[list[float]] = []
    #0 distance
    #1 number of stations
    drone_battery_need : list[float] = []
    #ration between distance and stations
    #iterate between drones
    for i in range(len(drones)):
        #append info on the drone
        drone_data.append([0,len(drones[i])-1])
        #iterate between stations
        for j in range(1,drone_data[i][1]):
            #add to the total distance the distance between the station and the next one
            drone_data[i][0] += distance(coordinate, drones[i][j], drones[i][j+1])
        #of the number of stations is not zero we can calculate the ratio
        if(drone_data[i][1] != 0):
            drone_battery_need.append(drone_data[i][0]/drone_data[i][1])
        else:
            drone_battery_need.append(0)
    #find drone with highest ratio
    return drone_battery_need.index(max(drone_battery_need)), drone_data

def main():
    drones : list[list[str]] = read_drones()
    coordinate : list[list[str]] = read_coordinate()

    drone_battery_need_id, drone_data = find_most_in_need_drone(drones, coordinate)

    print(f"highest battery capacity for {drones[drone_battery_need_id][0]}") 
    print(f"total distance = {drone_data[drone_battery_need_id][0]:f=2}")
    #minus one because the number of stop is one less than the number of stations visited
    print(f"number of stops = {drone_data[drone_battery_need_id][1]-1}")

if __name__ == "__main__":
    main()