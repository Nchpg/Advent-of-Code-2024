import numpy as np

def _try(a, b, n):
    if "?" in a:
        return False
    i = 0
    j = 0
    k = 0
    while i < n:
        if a[i] == '#':
            j+=1
        else:
            if j > 0:
                if k >= len(b):
                    return False
                if b[k] != j:
                    return False
                k+=1
            j = 0
        i+=1
    if a[-1] == '#':
        if k >= len(b):
            return False
        if b[k] != j:
            return False
        k += 1
    if k < len(b):
        return False
    return True

def _rec(a, b, i, n):
    c = 0
    while i < n:
        if a[i] == '?':
            a[i] = '#'
            c += _rec(a, b, i+1, n)
            a[i] = '.'
            c += _rec(a, b, i+1, n)
            a[i] = '?'
            return c
        i+=1
    return _try(a, b, n)

def get_nb_arr(l):
    a, b = l.split()
    a = list(a)
    b = b.split(",")
    for i,e in enumerate(b):
        b[i] = int(e)

    i = 0
    n = len(a)
    c = 0
    while i < n:
        if a[i] == '?':
            a[i] = '#'
            c += _rec(a, b, i+1, n)
            a[i] = '.'
            c += _rec(a, b, i+1, n)
            return c
        i+=1



with open("input.txt") as f:
    lines = [line.strip() for line in f]
    s = 0
    for l in lines:
        x = get_nb_arr(l)
        s += x
    print("[DAY12-1] Answer is", s)