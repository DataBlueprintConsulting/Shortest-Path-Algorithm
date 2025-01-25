import heapq
from collections import defaultdict

class State:
    def __init__(self, location, time, waiting_time):
        self.location = location
        self.time = time
        self.waiting_time = waiting_time

    def __lt__(self, other):
        return self.waiting_time > other.waiting_time

def max_waiting_time(B, L, locations, times):
    bus_stops = defaultdict(list)

    for bus in range(B):
        for stop in range(len(locations[bus])):
            loc = locations[bus][stop]
            time = times[bus][stop]
            bus_stops[loc].append((time, bus, stop))

    for stops in bus_stops.values():
        stops.sort(key=lambda x: x[0])

    queue = []
    heapq.heappush(queue, State(0, 0, 0))

    visited = set()

    max_wait = 0

    while queue:
        curr = heapq.heappop(queue)

        state_key = (curr.location, curr.time)
        if state_key in visited:
            continue
        visited.add(state_key)

        if curr.location == L - 1:
            max_wait = max(max_wait, curr.waiting_time)
            continue

        if curr.location not in bus_stops:
            continue
        stops = bus_stops[curr.location]

        first_valid_bus = 0
        while first_valid_bus < len(stops) and stops[first_valid_bus][0] < curr.time:
            first_valid_bus += 1

        for i in range(first_valid_bus, len(stops)):
            bus_time, bus, stop_index = stops[i]

            wait_time = bus_time - curr.time

            if stop_index < len(locations[bus]) - 1:
                next_loc = locations[bus][stop_index + 1]
                next_time = times[bus][stop_index + 1]

                heapq.heappush(queue, State(next_loc, next_time, curr.waiting_time + wait_time))

    return max_wait

def main():
    B, L = map(int, input().split()) 

    locations = []
    times = []

    for _ in range(B):
        bus_locations = list(map(int, input().strip().split()))
        bus_times = list(map(int, input().strip().split()))

        locations.append(bus_locations)
        times.append(bus_times)

    result = max_waiting_time(B, L, locations, times)
    print(result)

if __name__ == "__main__":
    main()