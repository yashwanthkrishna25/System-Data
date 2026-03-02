def parse_input():
    board = []
    changeable = []
    hinted = []
    for i in range(9):
        row = input().split()
        new_row = []
        for j, val in enumerate(row):
            if val.startswith("0"):  # Tina-filled
                changeable.append((i, j))
                new_row.append(int(val[1]))
            elif val.endswith("0"):  # Hinted
                hinted.append((i, j))
                new_row.append(int(val[:-1]))
            else:  # Pre-filled
                new_row.append(int(val))
        board.append(new_row)

    allowed_hints = list(map(int, input().split()))
    k = int(input())
    return board, changeable, hinted, allowed_hints, k

def is_valid(board, r, c, val):
    # Check row
    for j in range(9):
        if j != c and board[r][j] == val:
            return False
    # Check column
    for i in range(9):
        if i != r and board[i][c] == val:
            return False
    # Check 3x3 subgrid
    box_r, box_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if (i != r or j != c) and board[i][j] == val:
                return False
    return True

def find_wrong_cells(board, changeable, hinted, allowed_hints, k):
    wrong = []

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if (r, c) in hinted:
                if val not in allowed_hints or not is_valid(board, r, c, val):
                    wrong.append((r, c))
            elif (r, c) in changeable:
                if not is_valid(board, r, c, val):
                    wrong.append((r, c))

    return wrong

def main():
    board, changeable, hinted, allowed_hints, k = parse_input()
    wrong_cells = find_wrong_cells(board, changeable, hinted, allowed_hints, k)

    if len(wrong_cells) == 0:
        print("Won")
    elif len(wrong_cells) > k:
        print("Impossible")
    else:
        for r, c in sorted(wrong_cells):
            print(r, c)

main()
