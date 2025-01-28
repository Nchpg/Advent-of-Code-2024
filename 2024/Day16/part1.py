from AOC2024.aoc_tools import *
from collections import deque

REF_RES = 7036

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    g, (w, h) = npgrid(lines)
    sj, si = fnpgrid(g, 'S')[0]
    ej, ei = fnpgrid(g, 'E')[0]
    c = np.zeros((w, h))
    dio, djo = 1, 0
    q = deque([])
    for di, dj in cross:
        if g[sj+dj][si+di] == '.':
            c[sj+dj][si+di] = 1 + (1000 if di != dio and dj != djo else 0)
            q.append((si+di, sj+dj, di, dj))
    while len(q) > 0:
        i, j, dio, djo = q.pop()
        for di, dj in cross:
            if g[j + dj][i + di] in ".E":
                n = c[j][i] + 1 + (1000 if di != dio or dj != djo else 0)
                if n < c[j + dj][i + di] or c[j + dj][i + di] == 0:
                    c[j + dj][i + di] = n
                    q.append((i + di, j + dj, di, dj))

    return int(c[ej][ei])
























"""
Below is a model to compare the result with the expected one (not part of today's problem). 

The entry point of the problem is the manager function
"""
import ast
import sys
import pyperclip
sys.setrecursionlimit(10**8)
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