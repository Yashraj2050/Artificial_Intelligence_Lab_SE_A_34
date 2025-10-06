import heapq

# Graph representation
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start, 0, None))  # (f, node, g, parent)
    closed_list = {}
    step = 1

    print("\n--- A* Search Visualization ---\n")

    while open_list:
        f, current, g, parent = heapq.heappop(open_list)

        # Skip if already processed
        if current in closed_list:
            continue

        closed_list[current] = (g, parent)

        # Print current state
        print(f"Step {step}: Expanding node '{current}' with f={f}, g={g}, h={heuristics[current]}")
        step += 1

        # Goal test
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = closed_list[current][1]
            path.reverse()
            print("\nGoal reached!\n")
            return path, g

        # Expand neighbors
        for neighbor, cost in graph[current].items():
            g_new = g + cost
            f_new = g_new + heuristics[neighbor]
            heapq.heappush(open_list, (f_new, neighbor, g_new, current))

        # Display lists visually
        open_nodes = [item[1] for item in open_list]
        closed_nodes = list(closed_list.keys())
        print(f"  Open List: {open_nodes}")
        print(f"  Closed List: {closed_nodes}\n")

    return None, float('inf')

# Run A*
start, goal = 'S', 'G'
path, cost = a_star(graph, heuristics, start, goal)

print("Optimal Path Found:", " → ".join(path))
print("Total Path Cost:", cost)
