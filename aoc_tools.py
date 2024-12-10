import numpy as np
from tqdm import tqdm
import re

#GRID OFFSET
adj8 = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if i != 0 or j != 0]
corner = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if abs(i)+abs(j) == 2]
cross = [[i, j] for i in [-1, 0, 1]  for j in [-1, 0, 1]  if abs(i)+abs(j) == 1]

def d_tr(dx, dy):
    return dy, -dx

def g_tr(dx, dy):
    return dy, -dx

def nums(line):
    return [int(num) for num in re.findall(r'\d+', line)]

#Parse line into list of type t by delimiter d
def pl(l, d="", t=int):
    return list(map(t, l.split(d if d else None)))

#Cast list of type a in list of type t
def cl(l, t=int):
    return list(map(t, l))

#Parse list of line into list of list of type t by delimiter d
def pll(l, d="", t=int):
    return list(map(lambda x: list(map(t, x)), [[a.strip() for a in e.split(d if d else None) if a.strip()] for e in l]))

#Cast list of list of type a in list of list of type t
def cll(l, t=int):
    return list(map(lambda x: list(map(t, x)), [cl(e, t) for e in l if e]))

#Parse list of list in grid of type t
def grid(l, t=str):
    return [[t(a) for a in list(e) if a.strip()] for e in l if e]

def npgrid(l, t=str):
    g = np.array(grid(l, t))
    return g, g.shape

def cnpgrid(g, i, j):
    return 0 <= i < g.shape[0] and 0 <= j < g.shape[1]

def cvnpgrid(g, i, j, v):
    return cnpgrid(g, i, j) and g[i][j] == v

def pnpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield g[i][j]

def penpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield i, j, g[i][j]

def enpgrid(g):
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            yield i, j

def tqdm_enpgrid(g):
    return tqdm(enpgrid(g), total=g.shape[0]*g.shape[1])

def fnpgrid(g, x):
    for i, j in enpgrid(g):
        if g[i][j] == x:
            return i, j
    return None

def print_grid(g):
    print("="*g.shape[1])
    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
            print(g[i][j], end="")
        print()
    print("="*g.shape[1])
