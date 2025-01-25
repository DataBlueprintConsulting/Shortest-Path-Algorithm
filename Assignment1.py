import heapq
from collections import defaultdict

class Stop:
    def __init__(self, location, time, prev_location, bus_line):
        self.location = location
        self.time = time
        self.prev_location = prev_location
        self.bus_line = bus_line

def find_shortest_path(graph, start, end):
    min_time = [float('inf')] * len(graph)
    min_time[start] = 0

    pq = [(0, start)]

    while pq:
        time, loc = heapq.heappop(pq)

        if loc == end:
            return time

        if time > min_time[loc]:
            continue

        for next_loc, next_time, bus_line in graph[loc]:
            if time <= next_time and next_time < min_time[next_loc]:
                min_time[next_loc] = next_time
                heapq.heappush(pq, (next_time, next_loc))

    return -1 if min_time[end] == float('inf') else min_time[end]

def main():
    buses = int(input())
    locations_of_buses = int(input())

    graph = defaultdict(list)

    for _ in range(buses):
        locations = list(map(int, input().strip().split()))
        times = list(map(int, input().strip().split()))

        num_stops = len(locations)
        for i in range(num_stops):
            for j in range(i + 1, num_stops):
                graph[locations[i]].append((locations[j], times[j], _))

    min_time = find_shortest_path(graph, 0, locations_of_buses - 1)
    print(min_time)

if __name__ == "__main__":
    main()