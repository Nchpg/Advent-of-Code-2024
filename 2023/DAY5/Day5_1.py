def rec(P, s, i, _min):
    o = s
    if i >= len(P):
        if s < _min[0]:
            _min[0] = s
        return s
    b = False
    for e in P[i]:
        if e[1] <= o < e[1] + e[2]:
            s = o + e[0] - e[1]
            x = rec(P, s, i+1, _min)
            b = True
    if not b:
        rec(P, o, i + 1, _min)

    return _min[0]



with open("input.txt") as f:
    lines = f.read().split("\n\n")
    S = {}
    P = []

    for l in lines[1:]:
        x = l.strip().split("\n")
        i = 1
        for y in x[1:]:
            x[i] = y.split()
            j = 0
            for z in x[i]:
                x[i][j] = int(z)
                j+=1
            i+=1

        P.append(x[1:])

    seed=lines[0].split(": ")[1].split()
    for i in range(len(seed)):
        seed[i] = int(seed[i])

    m = [1000000000000]
    for s in seed:
        s = rec(P, s, 0, m)

    print("[DAY5-1] Answer is", m[0])


