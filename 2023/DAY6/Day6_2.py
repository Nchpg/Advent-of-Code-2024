
with open("input.txt") as f:
    lines = [ line.strip() for line in f ]

    D = lines[1].split()[1:]
    T = lines[0].split()[1:]
    D = int(''.join(D))
    T = int(''.join(T))

    nb = 0
    s = 1
    for j in range(T):
        if (T-j)*j > D:
            nb+=1

    s*=nb
    nb=0
    print("[DAY6-2] Answer is", s)