import math
D = [[0, 700, 200, math.inf, math.inf, math.inf],
     [700, 0, 300, 200, math.inf, 400],
     [200, 300, 0, 700, 600, math.inf],
     [math.inf, 200, 700, 0, 600, math.inf],
     [math.inf, math.inf, 600, 300, 0, 500],
     [math.inf, 400, math.inf, 100, 500, 0]
]
for k in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            D[i][j] = min(D[i][k] + D[k][j], D[i][j])
for i in range(len(D)):
    for j in range(i+1,len(D)):
        print("Длина маршрута между",i+1,'и',j+1,'—',D[i][j])