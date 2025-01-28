
with open("input.txt") as f:
    lines = [ line.strip() for line in f ]
    sum = 0
    for l in lines:
        w = l.split(";")

        _id = w[0].split(":")[0].split()[-1]
        w[0] = w[0].split(":")[1]
        L = [w[0].split()]
        i = 1
        for i in range(1, len(w)):
            L.append(w[i].split())
            i+=1
        b = True
        m = {'red': 0, 'blue': 0, 'green': 0}

        for c in L:
            s = {'red':0, 'blue':0, 'green':0}

            for i in range(0, len(c), 2):
                s[c[i+1].split(",")[0]] = int(c[i])
                m[c[i + 1].split(",")[0]] = max(int(c[i]),m[c[i + 1].split(",")[0]])

        if b:
            sum+=m['red'] * m['blue'] * m['green']
    print("[DAY2-2] Answer is", sum)