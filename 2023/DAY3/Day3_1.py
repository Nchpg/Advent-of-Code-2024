import numpy as np

def check_neighbours(M, i, j):
    n = len(M)
    m = len(M[0])
    for a in range(-1+i, 2+i):
        for b in range(-1+j, 2+j):
            if 0 <= a < n and 0 <= b < m:
                if M[a][b] == '#':
                    return False
    return True


with open("input.txt") as f:
    lines = [ line.strip() for line in f ]
    M = []
    for l in lines:
        M.append([])
        for c in l:
            if '0' <= c <= '9':
                M[-1].append(c)
            elif c != '.':
                M[-1].append('#')
            else:
                M[-1].append('.')
    M = np.array(M)

    n = len(M)
    m = len(M[0])
    i = 0
    j = 0
    s = 0
    while i < n:
        j = 0
        while j < m:
            if M[i][j] not in ['.', '#']:
                nb = 0
                b = False
                while j < m and M[i][j] not in ['.', '#']:
                    nb = nb*10+(ord(M[i][j])-ord('0'))
                    if not check_neighbours(M, i, j):
                        b = True
                    j+=1
                if b:
                    s += nb
            j+=1

        i+=1
    print("[DAY3-1] Answer is", s)


