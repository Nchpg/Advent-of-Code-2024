from collections import deque, defaultdict
from AOC2024.aoc_tools import *

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    g, (w, h) = npgrid(lines, str)
    c = np.zeros((w, h))
    sj, si = fnpgrid(g, 'S')[0]

    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        for di, dj in cross:
            if cnpgrid(g, i+di, j+dj) and g[j+dj][i+di] in '.E' and c[j+dj][i+di] == 0:
                c[j+dj][i+di] = c[j][i] + 1
                q.appendleft((i+di, j+dj))

    d = defaultdict(int)
    for i, j in enpgrid(c):
        for  di, dj in [(0, 1), (1, 0)]:
            if c[j][i] == 0 and cnpgrid(g, i+di, j+dj) and cnpgrid(g, i-di, j-dj) and g[j+dj][i+di] in 'SE.' and g[j-dj][i-di] in 'SE.':
                if abs(c[j+dj][i+di] - c[j-dj][i-di]) - 2 >= 100:
                    d[abs(c[j+dj][i+di] - c[j-dj][i-di]) - 2] += 1

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