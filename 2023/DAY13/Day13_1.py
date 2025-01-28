import numpy as np


def is_sym_l(M, l):
    i = 0
    while l-i >= 0 and l+1+i < len(M):
        if M[l-i] != M[l+1+i]:
            return False
        i+=1
    return True

def is_sym_c(M, c):
    i = 0
    while c-i >= 0 and c+1+i < len(M[0]):
        L1 = []
        for k in range(len(M)):
            L1.append(M[k][c-i])
        L2 = []
        for k in range(len(M)):
            L2.append(M[k][c+1+i])
        if L2 != L1:
            return False
        i+=1
    return True

with open("input.txt") as f:
    motif = f.read().split('\n\n')
    s = 0
    for m in motif:

        lines = m.split("\n")
        for i, l in enumerate(lines):
            lines[i] = list(l)

        for i in range(len(lines)-1):
            if is_sym_l(lines, i):
                s += (i+1)*100
        for i in range(len(lines[0])-1):
            if is_sym_c(lines, i):
                s += i+1

    print("[DAY13-1] Answer is", s)

