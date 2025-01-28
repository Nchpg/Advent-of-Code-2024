from AOC2024.aoc_tools import *

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    w = 101
    h = 103
    e = 100
    l = lnums(lines)
    g = np.array([[0]*w for _ in range(h)])
    for px, py, vx, vy in l:
        nx = (px + e*(vx+w))%w
        ny = (py + e*(vy+h))%h
        g[ny][nx] += 1

    for i in range(h):
        g[i][w//2] = 0
    for i in range(w):
        g[h//2][i] = 0

    q = [0, 0, 0, 0]
    for a, k in enumerate([0, w//2+1]):
        for b, l in enumerate([0, h//2+1]):
            for i in range(h//2):
                for j in range(w//2):
                    q[2*a+b] += g[l+i][k+j]
    t = q[0] * q[1] * q[2] * q[3]

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