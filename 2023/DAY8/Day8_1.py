with open("input.txt") as f:
    lines = [line.strip() for line in f]
    _ins = [*lines[0].strip()]
    A = {}
    for l in lines[2:]:
        a, b = (l.split("(")[1].strip()).split(")")[0].strip().split(",")
        a = a.strip()
        b = b.strip()
        A[l.split("=")[0].strip()] = {"L":a, "R":b}

    k = "AAA"
    step = 0

    while k != "ZZZ":
        for c in _ins:
            k = A[k][c]
            step +=1

    print("[DAY8-1] Answer is", step)