def min_G(inp):
    return min([G[m][inp] for m in range(n)])


with open('input.txt', 'r') as Inp:
    G = [list(map(float, line.split())) for line in Inp.read().split('\n')]
    print(' Input matrix: ')
    [print(*line) for line in G]

count = 0
for num in range(len(G)-2):
    print(f'\n Iteration №{num+1}')
    n = len(G)

    for i in range(n):
        min_line = min(G[i])
        if min_line != float('inf'):
            count += min_line
            for j in range(n):
                G[i][j] -= min_line
    [print(*line) for line in G]
    print()

    for j in range(n):
        min_row = min_G(j)
        if min_row != float('inf'):
            count += min_row
            for i in range(n):
                G[i][j] -= min_row
    [print(*line) for line in G]
    print('\t'*n, count)

    zeros = []
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0.0:
                G[i][j] = float('inf')
                zeros.append((min(G[i]) + min_G(j), i, j))
                G[i][j] = 0.0
    arg, v, u = max(zeros)
    G[u][v] = float('inf')
    for x in range(n):
        G[x][u] = float('inf')
        G[v][x] = float('inf')
    [print(*line) for line in G]