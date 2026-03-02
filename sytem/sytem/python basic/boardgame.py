from collections import deque

def is_valid(x, y, M, N, grid, visited):
    return 0 <= x < M and 0 <= y < N and grid[x][y] == 0 and not visited[x][y]

def get_neighbors(x, y, dx, dy):
    # Directions: forward, right, left, back
    directions = [
        (x + dx, y + dy),            # forward
        (x + dy, y - dx),            # right (90° clockwise)
        (x - dy, y + dx),            # left (90° counter-clockwise)
        (x - dx, y - dy)             # back (180°)
    ]
    return directions

def min_moves(grid, start, end, move_rule):
    M, N = len(grid), len(grid[0])
    visited = [[False] * N for _ in range(M)]
    queue = deque()
    
    sx, sy = start
    dx, dy = end
    step_x, step_y = move_rule
    
    queue.append((sx, sy, 0))
    visited[sx][sy] = True

    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == (dx, dy):
            return moves

        for nx, ny in get_neighbors(x, y, step_x, step_y):
            if is_valid(nx, ny, M, N, grid, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1  # If destination is unreachable

# Input section with prompts
print("Enter the number of rows and columns (M N): ")
M, N = map(int, input().split())

print(f"Enter the grid ({M} rows of {N} space-separated integers):")
grid = [list(map(int, input().split())) for _ in range(M)]

print("Enter the source cell coordinates (row column):")
sx, sy = map(int, input().split())

print("Enter the destination cell coordinates (row column):")
dx, dy = map(int, input().split())

print("Enter the move rule (dx dy):")
step_x, step_y = map(int, input().split())

# Output result
result = min_moves(grid, (sx, sy), (dx, dy), (step_x, step_y))
print("Minimum moves required to reach the destination:", result)