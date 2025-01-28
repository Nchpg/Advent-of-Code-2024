from AOC2024.aoc_tools import *

REF_RES = 9021

def move_h(g, xs, ys, dx, dy, e):
    g[ys][xs] = "."
    c = 1
    nb_O = 0
    while cnpgrid(g, ys + c * dy, xs + c * dx):
        if g[ys + c * dy][xs + c * dx] == "#":
            g[ys][xs] = "."
            ys -= dy
            xs -= dx
            i = 0
            while i < 2*nb_O:
                g[ys + (c - i) * dy][xs + (c - i) * dx] = (']' if e == ">" else '[')
                i += 1
                g[ys + (c - i) * dy][xs + (c - i) * dx] = ('[' if e == ">" else ']')
                i += 1
            g[ys + (c - i) * dy][xs + (c - i) * dx] = '@'
            tys, txs = ys + (c - i) * dy, xs + (c - i) * dx
            i += 1
            while c - i > 0:
                g[ys + (c - i) * dy][xs + (c - i) * dx] = '.'
                i += 1
            ys, xs = tys, txs
            break
        if g[ys + c * dy][xs + c * dx] == ('[' if e == ">" else ']') :
            c += 1
            nb_O += 1
        if g[ys + c * dy][xs + c * dx] == ".":
            g[ys][xs] = "."
            i = 0
            while i < 2 * nb_O:
                g[ys + (c - i) * dy][xs + (c - i) * dx] = (']' if e == ">" else '[')
                i += 1
                g[ys + (c - i) * dy][xs + (c - i) * dx] = ('[' if e == ">" else ']')
                i += 1
            g[ys + (c - i) * dy][xs + (c - i) * dx] = '@'
            tys, txs = ys + (c - i) * dy, xs + (c - i) * dx
            i += 1
            while c - i > 0:
                g[ys + (c - i) * dy][xs + (c - i) * dx] = '.'
                i += 1
            ys, xs = tys, txs
            break
        c += 1
    return xs, ys

def rec_find(L, g, e, dx, dy, C):
    R = []
    for x, y in L:
        if g[y + dy][x + dx] == "[":
            R.append([x + dx, y + dy])
            C.append([x + dx, y + dy])
            R.append([x + dx + 1, y + dy])
            C.append([x + dx + 1, y + dy])
            R = rec_find(R, g, e, dx, dy, C)
        elif g[y + dy][x + dx] == "]":
            R.append([x + dx, y + dy])
            C.append([x + dx, y + dy])
            R.append([x + dx - 1, y + dy])
            C.append([x + dx - 1, y + dy])
            R = rec_find(R, g, e, dx, dy, C)
        else:
            R.append([x, y])
    return R

def move_v(g, xs, ys, dx, dy, e):
    L  = []
    C = []
    C.append([xs, ys])
    C.append([xs+dx, ys+dy])
    L.append([xs+dx, ys+dy])
    if g[ys+dy][xs+dx] == "[":
        L.append([xs + dx + 1, ys + dy])
        C.append([xs + dx + 1, ys + dy])
    elif g[ys + dy][xs + dx] == "]":
        L.append([xs + dx - 1, ys + dy])
        C.append([xs + dx - 1, ys + dy])
    L = rec_find(L, g, e, dx, dy, C)
    good = True
    for x, y in L:
        if g[y + dy][x + dx] == "#":
            good = False
            break
    if good:
        g2 = g.copy()
        for x, y in C:
            g2[y][x] = '.'
        for x, y in C:
            g2[y + dy][x + dx] = g[y][x]
        xs += dx
        ys += dy
    else:
        g2 = g.copy()
    return xs, ys, g2


"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    p1, p2 = change_line_delim(lines, "\n\n")

    g, _ = npgrid(p1.split("\n"), str)
    g2 = []
    for l in g:
        g2.append([])
        for e in l:
            if e == "#":
                g2[-1] += "##"
            elif e == "O":
                g2[-1] += "[]"
            elif e == ".":
                g2[-1] += ".."
            elif e == "@":
                g2[-1] += "@."
    g2 = np.array(g2)
    g = g2
    ys, xs = fnpgrid(g, "@")[0]

    d = [e for e in p2 if e != "\n"]
    dirs = {">": [0, 1], "<": [0, -1], "^": [-1, 0], "v": [1, 0]}
    for e in d:
        dy, dx = dirs[e]
        if cvnpgrid(g, ys+dy, xs + dx,"#"):
            continue
        elif cvnpgrid(g, ys+dy, xs + dx, "[") or cvnpgrid(g, ys+dy, xs + dx, "]"):
            if e in "<>":
                xs, ys = move_h(g, xs, ys, dx, dy, e)
            else:
                xs, ys, g = move_v(g, xs, ys, dx, dy, e)
        elif cvnpgrid(g, ys + dy, xs + dx, "."):
            g[ys][xs] = "."
            xs += dx
            ys += dy
            g[ys][xs] = "@"
    return sum([100*x + y for x, y in fnpgrid(g, "[")])
























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