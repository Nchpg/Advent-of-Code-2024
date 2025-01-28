from AOC2024.aoc_tools import *

def find_region(g, i, j, v):
    m = 1
    v.add((i, j))
    for a, b in cross:
        if cvnpgrid(g, i+a, j+b, 1) and (i+a, j+b) not in v:
            m += find_region(g, i+a, j+b, v)
    return m

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    t = 0
    w = 101
    h = 103
    l = lnums(lines)
    g = np.array([[0]*w for _ in range(h)])
    for e in range(1, 10**6):
        g = np.array([[0] * w for _ in range(h)])
        for i, (px, py, vx, vy) in enumerate(l):
            nx = (px + 1*(vx+w))%w
            ny = (py + 1*(vy+h))%h
            l[i][0] = nx
            l[i][1] = ny
            g[ny][nx] = 1
        view = set()
        m = 0
        for i, j in enpgrid(g):
            if g[i][j] > 0:
                m = max(m, find_region(g, j, i , view))
        if m >= 200:
            t = e
            break

    g2 = np.array([['.']*w for _ in range(h)])

    for i in range(w):
        for j in range(h):
            g2[j][i] = '#' if g[j][i] else '.'

    print_grid(g2)

    return t
























"""
Below is a model to compare the result with the expected one (not part of today's problem). 

The entry point of the problem is the manager function
"""
import ast
import sys
import pyperclip
sys.setrecursionlimit(10**6)
def main(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        if len(lines) == 0:
            print(f"\033[1mFile {filename} is empty\033[0m")
            if filename == "ref":
                return True, "", "", True
            print("Killed")
            exit(0)
        ref = ""
        if filename == "ref":
            ref = REF_RES
        res = manager(lines)
        _type = None
        if type(res) == tuple and len(res) == 2:
            if res[1] in [int, float, tuple, list, str]:
                current, _type = res[0], res[1]
            else:
                print(f"\033[1mType ({res[2]}) not taken\033[0m")
                current = res
        else:
            current = res
        if ref != "":
            if _type is not None:
                if _type == list or _type == tuple:
                    ref = ast.literal_eval(ref)
                else:
                    ref = _type(ref)
                return ref == current, current, ref, False
            if type(current) == list or type(current) == tuple:
                ref = ast.literal_eval(ref)
            else:
                ref = type(current)(ref)

            return ref == current, current, ref, False
        return True, current, "", False

if __name__ == "__main__":
    pyperclip.copy("")
    if 'REF_RES' in vars():
        b, current, ref, ignored = main("ref")
        if ignored:
            print(f"--> Ref was ignored ⭕\n")
        elif b:
            print(f"\n--> Ref is valid ✅ : expected \033[1m{ref}\033[0m, get \033[1m{current}\033[0m\n")
        else:
            print(f"\n--> Ref is not valid ❌ : expected \033[1m{ref}\033[0m (type: {type(ref)}), get \033[1m{current}\033[0m (type: {type(current)})")
            print("Killed")
            exit(0)
    b, current, _, _  = main("input")
    if b:
        print(f"--> Result is \033[1m{current}\033[0m")
        pyperclip.copy(current)