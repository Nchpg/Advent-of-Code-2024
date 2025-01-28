from algo_py import queue
import sys
s = 0

def get_card(lines,P, v, A):
    if P.isempty():
        return v, P
    i = int(P.dequeue())
    if i >= len(lines)-1:
        return v, P
    l = lines[i-1]
    L1 = l.split(":")[1].split("|")[0].strip().split(" ")
    L2 = l.split(":")[1].split("|")[1].strip().split(" ")

    k = 0
    V = []


    for e in L2:
        if e in L1 and e not in V and e != '':
            v += 1
            V.append(e)
            k+=1
            P.enqueue(i+k)


    return v,P


with open("input.txt") as f:
    lines = [ line.strip() for line in f ]

    A = []
    for l in lines:
        v =0
        L1 = l.split(":")[1].split("|")[0].strip().split(" ")
        L2 = l.split(":")[1].split("|")[1].strip().split(" ")



        V = []
        for e in L2:
            if e in L1 and e not in V and e != '':
                if v==0:
                    v = 1
                else:
                    v*=2

        s+=v




    M = []
    P = queue.Queue()
    v = len(lines)

    for i in range(len(lines)):
        P.enqueue(i)
        while not P.isempty():
            v, P = get_card(lines, P, v, A)

    print("[DAY4-2] Answer is", v)