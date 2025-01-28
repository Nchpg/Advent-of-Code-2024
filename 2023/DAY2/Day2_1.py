
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
        for c in L:
            s = {'red':0, 'blue':0, 'green':0}

            for i in range(0, len(c), 2):
                s[c[i+1].split(",")[0]] = int(c[i])

            if s['red'] > 12 or s['green']>13 or s['blue']>14:
                b = False

        if b:
            sum+=int(_id)
    print("[DAY2-1] Answer is", sum)