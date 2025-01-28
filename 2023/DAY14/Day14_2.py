import numpy as np
from functools import cache, lru_cache


def cost(M):
    s = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'O':
                s+=(len(M)-i)
    return s

@lru_cache(maxsize=100000000)
def cycle(M):
    res = []
    for i in range(len(M)):
        res.append([])
        for j in range(len(M[0])):
            res[i].append(M[i][j])

    for i in range(1, len(M)):
        for j in range(len(M[0])):
            if res[i][j] == 'O':
                k = 1
                while i-k >= 0 and res[i-k][j] == '.':
                    res[i-k+1][j] = '.'
                    res[i-k][j] = 'O'
                    k+=1
    for j in range(1, len(M[0])):
        for i in range(len(M)):
            if res[i][j] == 'O':
                k = 1
                while j-k >= 0 and res[i][j-k] == '.':
                    res[i][j-k+1] = '.'
                    res[i][j-k] = 'O'
                    k+=1
    for i in range(len(M)-2, -1, -1):
        for j in range(len(M[0])):
            if res[i][j] == 'O':
                k = 1
                while i+k < len(res) and res[i+k][j] == '.':
                    res[i+k-1][j] = '.'
                    res[i+k][j] = 'O'
                    k+=1
    for j in range(len(M[0])-2, -1, -1):
        for i in range(len(M)):
            if res[i][j] == 'O':
                k = 1
                while j+k < len(M[0]) and res[i][j+k] == '.':
                    res[i][j+k-1] = '.'
                    res[i][j+k] = 'O'
                    k+=1
    M = []
    for i in range(len(res)):
        M.append(tuple(res[i]))
    M = tuple(M)
    return M

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    for i, l in enumerate(lines):
        lines[i] = tuple(l)
    M = tuple(lines)
    Possi = {}
    for i in range(1100):
        if i > 1000:
            m = cost(M)
            if m in Possi:
                Possi[m] = [Possi[m][0], i-Possi[m][2], i]
            else:
                Possi[m] = [i, i, i]
        M = cycle(M)
    M = np.array(M)
    L = []
    for k, (s, p, _) in Possi.items():
        if (1000000000-s)%p == 0:
            L.append(str(k))
    print("[DAY14-2] Answer is", " or ".join(L))