def decomp(n):
    L = dict()
    k = 2
    while n != 1:
        exp = 0
        while n % k == 0:
            n = n // k
            exp += 1
        if exp != 0:
            L[k] = exp
        k = k + 1

    return L
def _ppcm(a, b):
    Da = decomp(a)
    Db = decomp(b)
    p = 1
    for facteur, exposant in Da.items():
        if facteur in Db:
            exp = max(exposant, Db[facteur])
        else:
            exp = exposant

        p *= facteur ** exp

    for facteur, exposant in Db.items():
        if facteur not in Da:
            p *= facteur ** exposant

    return p

def ppcm(*args):
    L = list(args)
    while len(L) > 1:
        a = L[-1]
        L.pop()
        b = L[-1]
        L.pop()
        L.append(_ppcm(a, b))

    return L[0]


with open("input.txt") as f:
    lines = [line.strip() for line in f]
    _ins = [*lines[0].strip()]
    A = {}
    start = []
    for l in lines[2:]:
        a, b = (l.split("(")[1].strip()).split(")")[0].strip().split(",")
        a = a.strip()
        b = b.strip()
        c = l.split("=")[0].strip()
        if c[-1] == "A":
            start.append(c)
        A[c] = {"L":a, "R":b}

    step = 0
    n = len(start)
    b = False
    i = 0
    for s in start:
        step = 0
        while not b:
            for c in _ins:
                s = A[s][c]
                step +=1
            if s[-1] == "Z":
                break
        start[i] = step
        i+=1

    s = start[0]
    for k in range(1, len(start)):
        s = ppcm(s, start[k])
    print("[DAY8-2] Answer is", s)