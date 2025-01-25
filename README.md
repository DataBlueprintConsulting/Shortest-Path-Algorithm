## 🧠 Algorithm Used: Modified Dijkstra's Algorithm

This project uses a **Modified Dijkstra's Algorithm** to solve the problem of determining the maximum waiting time while traveling between locations on a set of bus routes.

### Key Features of the Algorithm
1. **Priority Queue**:
   - The algorithm uses a priority queue to process states based on their waiting time, ensuring that the states with the highest waiting time are processed first.

2. **Graph Representation**:
   - The bus routes are modeled as a weighted graph:
     - **Nodes**: Represent bus stops (locations).
     - **Edges**: Represent bus routes between stops, with weights as travel times.

3. **Optimization Metric**:
   - Unlike traditional Dijkstra's algorithm that minimizes the cost or distance, this algorithm **maximizes the waiting time** while ensuring the path is valid.

4. **Relaxation Process**:
   - At each stop, the algorithm evaluates all possible next bus stops (or transfers) and calculates the additional waiting time required. It updates the state if this results in a longer waiting time.

5. **Handling Transfers**:
   - The algorithm considers possible transfers between buses at a given location and ensures that only valid connections (i.e., those arriving after the current stop's time) are processed.

### Why Modified Dijkstra's Algorithm?
This approach is ideal for problems involving optimization over a graph with weighted edges. By modifying the standard Dijkstra's algorithm, this implementation finds a valid path with the **maximum waiting time**, which aligns with the problem's requirements.

### Algorithm Flow
1. Initialize a priority queue with the starting location (e.g., location `0`) and a waiting time of `0`.
2. For each state processed:
   - Check if the destination has been reached and update the maximum waiting time if necessary.
   - Process all buses stopping at the current location and evaluate transfers to subsequent stops.
   - Add valid transitions to the priority queue for further processing.
3. Return the maximum waiting time once all valid paths have been explored.

This approach ensures an efficient traversal of the graph and computes the optimal waiting time while avoiding cycles through a visited state tracking mechanism.
