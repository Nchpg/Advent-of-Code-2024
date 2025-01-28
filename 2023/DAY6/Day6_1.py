
with open("input.txt") as f:
    lines = [ line.strip() for line in f ]

    D = lines[1].split()[1:]
    T = lines[0].split()[1:]

    for i in range(len(T)):
        T[i] = int(T[i])
        D[i] = int(D[i])

    nb = 0
    s = 1
    for i in range(len(D)):
        for j in range(T[i]):
            if (T[i]-j)*j > D[i]:
                nb+=1
        s*=nb
        nb=0

    print("[DAY6-1] Answer is", s)