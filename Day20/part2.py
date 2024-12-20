from collections import deque, defaultdict
from AOC2024.aoc_tools import *

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    g, (w, h) = npgrid(lines, str)
    c = np.zeros((w, h))
    sj, si = fnpgrid(g, 'S')[0]

    path = set()
    path.add((si, sj))
    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        for di, dj in cross:
            if cnpgrid(g, i+di, j+dj) and g[j+dj][i+di] in '.E' and c[j+dj][i+di] == 0:
                c[j+dj][i+di] = c[j][i] + 1
                path.add((i+di, j+dj))
                q.appendleft((i+di, j+dj))

    d = defaultdict(int)
    cheat = set()
    for i, j in path:
        seen = set()
        seen.add((i, j))
        oi, oj = i, j
        q = deque([(i, j, 0)])
        while q:
            i, j, nb = q.popleft()
            if g[j][i] in "S.E" and (oi, oj, i, j) not in cheat and abs(c[j][i] - c[oj][oi]) - nb >= 100:
                d[int(abs(c[j][i] - c[oj][oi]) - nb)] += 1
                cheat.add((i, j, oi, oj))
            if nb < 20:
                for di, dj in cross:
                    if cnpgrid(g, i + di, j + dj) and (i+di, j+dj) not in seen:
                        seen.add((i+di, j+dj))
                        q.append((i + di, j + dj, nb + 1))


    return sum([v for v in d.values()])
























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