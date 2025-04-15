import heapq
import time

goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def h_misplaced(state):
    return sum(
        1 for i in range(3) for j in range(3)
        if state[i][j] != 0 and state[i][j] != goal_state[i][j]
    )

def gbfs(start):
    visited = set()
    pq = []
    heapq.heappush(pq, (h_misplaced(start), start, []))
    nodes_expanded = 0
    start_time = time.time()

    while pq:
        _, current, path = heapq.heappop(pq)

        if current == goal_state:
            return path + [current], time.time() - start_time, nodes_expanded

        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(pq, (h_misplaced(neighbor), neighbor, path + [current]))

    return None, time.time() - start_time, nodes_expanded

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print("-----")

# Contoh start state
start_state = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

print("Greedy Best-First Search (GBFS):")
path, exec_time, nodes = gbfs(start_state)
print_path(path)
print(f"Steps: {len(path)-1}, Time: {exec_time:.4f}s, Nodes: {nodes}")
