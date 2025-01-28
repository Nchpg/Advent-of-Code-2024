import numpy as np
from algo_py import stack

def get_o(c):
    if c == '|':
        return 'n', 's'
    if c == '-':
        return 'e', 'o'
    if c == 'F':
        return 'n', 'o'
    if c == 'J':
        return 's', 'e'
    if c == 'L':
        return 's', 'o'
    if c == '7':
        return 'e', 'n'
    return None, None

def get_opp(o):
    if o == 's':
        return 'n'
    if o == 'n':
        return 's'
    if o == 'e':
        return 'o'
    if o == 'o':
        return 'e'
def get_new_coor(x, y, o):
    if o == 'n':
        return x, y-1
    if o == 's':
        return x, y+1
    if o == 'o':
        return x-1, y
    if o == 'e':
        return x+1, y
    print("ERROR")
    exit(1)
def prop(M, x, y, o, R, c):
    a, b = get_o(M[y][x])
    if o in [a,b]:
        R[y][x] = c
        if o == a:
            o = b
        else:
            o = a
        o = get_opp(o)
        x, y = get_new_coor(x, y, o)
        if R[y][x] == '0':
            return c+1
        return prop(M, x, y, o, R, c+1)
    return 0

def prop2(M, R, s):
    c = 0
    while not s.isempty():
        x, y, o, c = s.pop()
        a, b = get_o(M[y][x])
        if o in [a, b]:
            R[y][x] = c
            if o == a:
                o = b
            else:
                o = a
            o = get_opp(o)
            x, y = get_new_coor(x, y, o)
            if R[y][x] == '0':
                return c + 1
            s.push((x, y, o, c + 1))
    return c

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    s = 0
    M = []
    x, y = 0,0
    for l in lines:
        M.append([*l.strip()])
        if 'S' in M[-1]:
            y = len(M)-1
            x = M[-1].index("S")
    M = np.array(M)
    R = np.full((len(M), len(M[0])), '.')
    R[y][x] = 0
    s=  stack.Stack()
    s.push((x-1, y, 'o', 1))
    m = prop2(M, R, s)
    s.push((x, y+1, 's', 1))
    m1 = prop2(M, R, s)
    s.push((x, y-1, 'n', 1))
    m2 = prop2(M, R, s)
    s.push((x+1, y, 'e', 1))
    m3 = prop2(M, R, s)

    print("[DAY10-1] Answer is", int(max(m1,m2,m3,m)/2))