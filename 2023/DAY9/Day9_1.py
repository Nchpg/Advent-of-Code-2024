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

        L[-1].append(0)
        for i in range(len(L)-2, -1, -1):
            L[i].append(L[i+1][-1]+L[i][-1])

        s+=L[0][-1]
    print("[DAY9-1] Answer is", s)