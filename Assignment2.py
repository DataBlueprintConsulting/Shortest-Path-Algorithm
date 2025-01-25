import heapq
from collections import defaultdict, namedtuple

class Stop:
    def __init__(self, location, time, bus_line, stop_index):
        self.location = location
        self.time = time
        self.bus_line = bus_line
        self.stop_index = stop_index

class State:
    def __init__(self, bus_line, stop_index, wait_time, current_time):
        self.bus_line = bus_line
        self.stop_index = stop_index
        self.wait_time = wait_time
        self.current_time = current_time

    def __lt__(self, other):
        return self.wait_time < other.wait_time

def find_min_wait_time(bus_routes, stops_by_location, home_location):
    pq = []
    visited = set()

    initial_stops = stops_by_location[0]
    for stop in initial_stops:
        initial_wait = stop.time 
        heapq.heappush(pq, State(stop.bus_line, stop.stop_index, initial_wait, stop.time))

    while pq:
        current = heapq.heappop(pq)
        current_route = bus_routes[current.bus_line]
        current_stop = current_route[current.stop_index]

        if current_stop.location == home_location:
            return current.wait_time

        state_key = (current.bus_line, current.stop_index, current.current_time)
        if state_key in visited:
            continue
        visited.add(state_key)

        for i in range(current.stop_index + 1, len(current_route)):
            next_stop = current_route[i]
            heapq.heappush(pq, State(
                current.bus_line,
                i,
                current.wait_time, 
                next_stop.time
            ))

        possible_transfers = stops_by_location[current_stop.location]
        for next_stop in possible_transfers:
            if next_stop.time > current_stop.time and next_stop.bus_line != current.bus_line:
                transfer_wait_time = next_stop.time - current_stop.time
                heapq.heappush(pq, State(
                    next_stop.bus_line,
                    next_stop.stop_index,
                    current.wait_time + transfer_wait_time,
                    next_stop.time
                ))

    return 0 

def main():
    B = int(input())  
    L = int(input()) 

    bus_routes = []
    stops_by_location = defaultdict(list)

    for b in range(B):
        locations = list(map(int, input().strip().split()))
        times = list(map(int, input().strip().split()))
        
        route = []
        for i in range(len(locations)):
            stop = Stop(locations[i], times[i], b, i)
            route.append(stop)
            stops_by_location[stop.location].append(stop)
        bus_routes.append(route)

    for stops in stops_by_location.values():
        stops.sort(key=lambda x: x.time)

    result = find_min_wait_time(bus_routes, stops_by_location, L - 1)
    print(result)

if __name__ == "__main__":
    main()