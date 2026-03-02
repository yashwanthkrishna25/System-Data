def min_string_factor(X, Y, S, R):
    from collections import deque

    len_x = len(X)
    len_y = len(Y)
    reversed_Y = Y[::-1]

    # Build all possible substrings from Y and reversed Y using a Trie-based method (greedy approach)
    dp = [float('inf')] * (len_x + 1)  # dp[i] = min string factor to build X[:i]
    count = [(0, 0)] * (len_x + 1)     # number of (normal, reversed) substrings used
    dp[0] = 0

    for i in range(len_x):
        if dp[i] == float('inf'):
            continue

        # Try matching with forward Y
        for j in range(i + 1, len_x + 1):
            substr = X[i:j]
            if substr in Y:
                if dp[j] > dp[i] + S:
                    dp[j] = dp[i] + S
                    count[j] = (count[i][0] + 1, count[i][1])
                elif dp[j] == dp[i] + S:
                    if count[j][0] + count[j][1] > count[i][0] + 1 + count[i][1]:
                        count[j] = (count[i][0] + 1, count[i][1])

        # Try matching with reversed Y
        for j in range(i + 1, len_x + 1):
            substr = X[i:j]
            if substr in reversed_Y:
                if dp[j] > dp[i] + R:
                    dp[j] = dp[i] + R
                    count[j] = (count[i][0], count[i][1] + 1)
                elif dp[j] == dp[i] + R:
                    if count[j][0] + count[j][1] > count[i][0] + count[i][1] + 1:
                        count[j] = (count[i][0], count[i][1] + 1)

    return dp[len_x] if dp[len_x] != float('inf') else "Impossible"

# Input prompts
print("Enter string X:")
X = input().strip()
print("Enter string Y:")
Y = input().strip()
print("Enter two integers S and R separated by space:")
S, R = map(int, input().split())

# Compute and print result
result = min_string_factor(X, Y, S, R)
print("Output:")
print(result)
