with open("input.txt") as f:
    lines = [ line.strip() for line in f ]
    M = []
    s= 0
    for l in lines:
        v =0
        L1 = l.split(":")[1].split("|")[0].strip().split(" ")
        L2 = l.split(":")[1].split("|")[1].strip().split(" ")



        V = []
        for e in L2:
            if e in L1 and e not in V and e != '':
                V.append(e)
                if v==0:
                    v = 1
                else:
                    v*=2
        s+=v

    print("[DAY4-1] Answer is", s)