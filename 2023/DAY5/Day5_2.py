def T_(x, start, end):
    return x+start-end

def prop(Range, tuples):
    F = []
    for (d, start, r) in tuples:
        end = start+r
        E = []
        while Range:
            a, b = Range.pop()

            # [a]                       |b]
            #      [start         end]
            #      [m]             [n]

            m = start
            n = end
            if a >= start:
                m = a
            if b <= end:
                n = b

            # CHECK INTERSECTION

            # [a]                       |b]
            #      [start       end]
            #      [m]###########[n]

            #       [a]                       |b]
            # [start             end]
            #       [m]###########[n]

            #       [a]                       |b]
            #                  [start                 end]
            #                  [m]##########[n]

            #       [a]                       |b]
            #  [start                               end]
            #       [m]#######################[n]
            if n > a and b > m:
                F.append((T_(m, d, start), T_(n, d, start)))

            # Check semi_intersection
            # BEFORE

            # [a]                       |b]
            #      [start       end]
            # #####[m]           [n]

            #       [a]                       |b]
            #                  [start                 end]
            #       ###########[m]            [n]

            #       [a]                       |b]
            #                                       [start                 end]
            #       ##########################[n]   [m]

            if m != a:
                E.append((a, min(n, m)))

            # AFTER

            # [a]                       |b]
            #      [start       end]
            #      [m]           [n]####

            #                       [a]                       |b]
            #  [start     end]
            #              [n]   [m]##########################
            elif n != b:
                E.append((max(n, m), b))

        Range = E
    return F+Range


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

    seed2 = []
    for i in range(0,len(seed),2):
        seed2.append((seed[i],seed[i]+seed[i+1]))

    res = []
    for a, b in seed2:
        R = [(a, b)]
        for i in range(len(P)):
            R = prop(R, P[i])
        # print(len(R))
        res.append(min(R)[0])

    print("[DAY5-2] Answer is", min(res))


