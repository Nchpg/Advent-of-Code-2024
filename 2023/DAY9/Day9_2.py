def only_zero(L):
    for e in L:
        if e != 0:
            return False
    return True


with open("input.txt") as f:
    lines = [line.strip() for line in f]
    s = 0
    for l in lines:
        L = l.split()
        for i,e in enumerate(L):
            L[i] = int(e)
        L = [L]
        while not only_zero(L[-1]):
            L.append([])
            for i in range(len(L[-2])-1):
                L[-1].append(L[-2][i+1] - L[-2][i])

        L[-1].insert(0, 0)
        for i in range(len(L)-2, -1, -1):
            L[i].insert(0, -L[i+1][0]+L[i][0])

        s+=L[0][0]
    print("[DAY9-2] Answer is", s)