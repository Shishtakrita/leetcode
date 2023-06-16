class UndergroundSystem:

    def __init__(self):
        self.ongoing_trips = {}
        self.completed_trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if id in self.ongoing_trips:
        #     raise Exception(
        #         'Cannot check in now for {}, trip from {} is already in progress'.format(id, self.ongoing_trips[id]))
        self.ongoing_trips[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # if id not in self.ongoing_trips:
        #     raise Exception('Invalid check out for {}, there is no existing trip in progress'.format(id))
        trip = self.ongoing_trips.pop(id)
        from_station = trip[0]
        travel_time = t - trip[1]

        key = (from_station, stationName)
        self.completed_trips[key] = (
            self.completed_trips.get(key, (0, 0))[0] + travel_time, self.completed_trips.get(key, (0, 0))[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        print(self.completed_trips[key][0] / self.completed_trips[key][1])
        return self.completed_trips[key][0] / self.completed_trips[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


if __name__ == '__main__':
    ug = UndergroundSystem()
    ug.checkIn(45, "Leyton", 3)
    ug.checkIn(32, "Paradise", 8)
    ug.checkIn(27, "Leyton", 10)
    ug.checkOut(45, "Waterloo", 15)
    ug.checkOut(27, "Waterloo", 20)  # Customer   27 "Leyton" -> "Waterloo" in 20 - 10 = 10
    ug.checkOut(32, "Cambridge", 22)  # Customer  32 "Paradise" -> "Cambridge" in 22 - 8 = 14
    ug.getAverageTime("Paradise", "Cambridge")  # return 14.00000. Onetrip "Paradise" -> "Cambridge", (14) / 1 = 14
    ug.getAverageTime("Leyton", "Waterloo")  # return 11.00000.Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
    ug.checkIn(10, "Leyton", 24)
    ug.getAverageTime("Leyton", "Waterloo")  # return 11.00000
    ug.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38 - 24 = 14
    ug.getAverageTime("Leyton",
                      "Waterloo")  # return 12.00000.Three trips"Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

    print(ug.ongoing_trips)
    print(ug.completed_trips)
