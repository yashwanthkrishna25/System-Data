def is_valid(grid):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            if grid[i][j] != 0:
                if row[grid[i][j]]:
                    return False
                row[grid[i][j]] = 1
            if grid[j][i] != 0:
                if col[grid[j][i]]:
                    return False
                col[grid[j][i]] = 1

    for box_row in range(3):
        for box_col in range(3):
            box = [0] * 10
            for i in range(3):
                for j in range(3):
                    val = grid[3*box_row + i][3*box_col + j]
                    if val != 0:
                        if box[val]:
                            return False
                        box[val] = 1
    return True

def parse_input():
    print("Enter the 9x9 Sudoku Grid (each row space-separated, using special format):")
    print("→ Use '0X' (e.g., 05) for Tina-filled numbers")
    print("→ Use 'X0' (e.g., 30) for Hint values")
    print("→ Use 'X' (e.g., 4) for pre-filled values")
    grid = []
    meta = []
    for row_num in range(9):
        row = input(f"Row {row_num + 1}: ").split()
        grid_row = []
        meta_row = []
        for num in row:
            if num.endswith('0') and not num.startswith('0'):
                grid_row.append(int(num[:-1]))
                meta_row.append('H')  # Hint
            elif num.startswith('0') and not num.endswith('0'):
                grid_row.append(int(num[1:]))
                meta_row.append('T')  # Tina filled
            else:
                grid_row.append(int(num))
                meta_row.append('P')  # Prefilled
        grid.append(grid_row)
        meta.append(meta_row)

    print("Enter the allowed hint values (space-separated):")
    hint_values = list(map(int, input().split()))
    print("Enter the maximum allowed incorrect cells (K):")
    k = int(input())
    return grid, meta, hint_values, k

def solve(grid, meta, hint_values, k):
    from copy import deepcopy

    def can_place(i, j, val):
        for x in range(9):
            if grid[i][x] == val or grid[x][j] == val:
                return False

        bi, bj = 3 * (i//3), 3 * (j//3)
        for r in range(bi, bi+3):
            for c in range(bj, bj+3):
                if grid[r][c] == val:
                    return False
        return True

    wrong_cells = []

    for i in range(9):
        for j in range(9):
            if meta[i][j] in {'T', 'H'}:
                val = grid[i][j]
                if not can_place(i, j, val):
                    wrong_cells.append((i, j))

    print("\n✅ Output:")
    if len(wrong_cells) == 0:
        print("Won")
    elif len(wrong_cells) > k:
        print("Impossible")
    else:
        for i, j in wrong_cells:
            print(i, j)

# Run the complete program
grid, meta, hint_values, k = parse_input()
solve(grid, meta, hint_values, k)
