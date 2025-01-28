import numpy as np


def is_sym_c(M, c):
    i = 0
    d = 0
    b = False

    while c-i >= 0 and c+1+i < len(M[0]):
        L1 = []
        for k in range(len(M)):
            L1.append(M[k][c-i])
        L2 = []
        for k in range(len(M)):
            L2.append(M[k][c+1+i])

        if L2 != L1:
            for k in range(len(M)):
                if L2[k] != L1[k]:
                    d +=1
            if d > 1 or b:
                return False
            if d == 1 and not b:
                b = True
        i+=1
    return b


def is_sym_l(M, l):
    i = 0
    d = 0
    b = False
    while l-i >= 0 and l+1+i < len(M):
        if M[l-i] != M[l+1+i]:
            d = 0
            for j in range(len(M[0])):
                if M[l-i][j] != M[l+1+i][j]:
                    d += 1
            if d > 1 or b:
                return False
            if d == 1 and not b:
                b = True
        i+=1
    return b


with open("input.txt") as f:
    motif = f.read().split('\n\n')
    s = 0
    for m in motif:
        lines = m.split("\n")
        for i, l in enumerate(lines):
            lines[i] = list(l)
        for i in range(len(lines[0])-1):
            if is_sym_c(lines, i):
                s += (i+1)
        for i in range(len(lines)-1):

            if is_sym_l(lines, i):
                s += (i+1)*100

    print("[DAY13-2] Answer is", s)

