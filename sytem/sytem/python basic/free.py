def max_expertise(n, c, conflicts, expertise):
    from itertools import combinations

    # Build conflict graph (adjacency list)
    conflict_graph = [set() for _ in range(n)]
    for u, v in conflicts:
        conflict_graph[u - 1].add(v - 1)
        conflict_graph[v - 1].add(u - 1)

    # Since it's NP-hard, use greedy + bitmasking for small components
    visited = [False] * n
    max_total = 0

    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in conflict_graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            size = len(component)

            # Bitmask to try all combinations within the component
            best = 0
            for mask in range(1 << size):
                valid = True
                total = 0
                chosen = []
                for j in range(size):
                    if (mask >> j) & 1:
                        for k in chosen:
                            if component[j] in conflict_graph[component[k]]:
                                valid = False
                                break
                        if not valid:
                            break
                        chosen.append(j)
                        total += expertise[component[j]]
                if valid:
                    best = max(best, total)
            max_total += best

    return max_total

# -------- INPUT AND OUTPUT --------

print("Enter number of employees and number of conflicts (n c):")
n, c = map(int, input().split())

print(f"Enter {c} pairs of conflicts (1-based index):")
conflicts = [tuple(map(int, input().split())) for _ in range(c)]

print(f"Enter {n} space-separated expertise values:")
expertise = list(map(int, input().split()))

# Compute and print output
result = max_expertise(n, c, conflicts, expertise)
print("Output:")
print(result)
