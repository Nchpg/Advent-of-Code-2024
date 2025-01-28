import numpy as np

def check_neighbours(M, i, j):
    n = len(M)
    m = len(M[0])
    for a in range(-1+i, 2+i):
        for b in range(-1+j, 2+j):
            if 0 <= a < n and 0 <= b < m:
                if M[a][b] == '#':
                    return False, str(a)+'_'+str(b)
    return True, "0"


with open("input.txt") as f:
    lines = [ line.strip() for line in f ]
    M = []
    for l in lines:
        M.append([])
        for c in l:
            if '0' <= c <= '9':
                M[-1].append(c)
            elif c == '*':
                M[-1].append('#')
            else:
                M[-1].append('.')
    M = np.array(M)

    n = len(M)
    m = len(M[0])
    i = 0
    j = 0
    s = 0
    L = {}
    key = []
    while i < n:
        j = 0
        while j < m:
            if M[i][j] not in ['.', '#']:
                nb = 0
                b = False
                key = []
                while j < m and M[i][j] not in ['.', '#']:
                    nb = nb*10+(ord(M[i][j])-ord('0'))
                    r, k =  check_neighbours(M, i, j)
                    if not r:
                        if k not in key:
                            key.append(k)
                        b = True
                    j+=1
                if b:
                    for ke in key:
                        if ke in L:
                            L[ke].append(nb)
                        else:
                            L[ke] = [nb]
            j+=1

        i+=1

    s = 0
    for c in L.values():
        if len(c) == 2:
            s+=c[0]*c[1]
    print("[DAY3-2] Answer is", s)


