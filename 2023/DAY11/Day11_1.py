import numpy as np
from algo_py import queue
def comput_dist(a, b, mx, my):
    T = np.full((mx, my), -1)
    x1,y1=a.split("_")
    x1 = int(x1)
    y1 = int(y1)
    T[x1][y1] = 0
    x2, y2 = b.split("_")
    x2 = int(x2)
    y2 = int(y2)
    c = 0
    q = queue.Queue()
    q.enqueue((x1, y1, 0))
    while not q.isempty():
        x, y, c = q.dequeue()
        if x == x2 and y == y2:
            return c
        if x != x2:
            if x < x2:
                q.enqueue((x + 1, y, c + 1))
            else:
                q.enqueue((x - 1, y, c + 1))
        else:
            if y < y2:
                q.enqueue((x, y + 1, c + 1))
            else:
                q.enqueue((x, y - 1, c + 1))

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    M = []
    for l in lines:
        M.append(list(l))
        if not "#" in l:
            M.append(list(l))

    for x in range(len(M[0])-1, -1, -1):
        i = 0
        for y in range(len(M)):
            if M[y][x] == '.':
                i+=1
            else:
                break
        if i == len(M):
            for y in range(len(M)):
                M[y].insert(x, ".")

    G = []
    for y in range(len(M)):
        for x in range(len(M[0])):
            if M[y][x] == "#":
                G.append("_".join([str(x), str(y)]))
    M = np.array(M)

    s = 0
    for i in range(len(G)):
        for j in range(i+1, len(G)):
            x = comput_dist(G[i], G[j], len(M[0]), len(M))
            s += x

    print("[DAY11-1] Answer is", s)