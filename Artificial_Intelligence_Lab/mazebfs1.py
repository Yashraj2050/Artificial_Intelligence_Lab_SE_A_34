from collections import deque

def bfs(maze, start, end):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])            # Queue for BFS
    visited = set([start])            # Track visited cells
    parent = {start: None}            # Store the parent of each cell

    while queue:
        current = queue.popleft()
        if current == end:
            break  # Exit found

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] != '#' and
                    next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current  # Track path

    # Reconstruct path from end to start
    if end in parent:
        path = []
        current = end
        while current:
            path.append(current)
            current = parent[current]
        path.reverse()  # From start to end

        # Optionally, mark the path in the maze (without modifying 'S' and 'E')
        for r, c in path:
            if maze[r][c] not in ('S', 'E'):
                maze[r][c] = '*'

        return path  # Return the actual path
    else:
        return None  # No path found

# Maze definition
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

# Run BFS and get path
path = bfs(maze, start, end)

if path:
    print("Path found:")
    for step in path:
        print(step)
    
    print("\nMaze with path marked ('*'):")
    for row in maze:
        print(' '.join(row))
else:
    print("No path exists.")
