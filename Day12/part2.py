from AOC2024.aoc_tools import *


REF_RES = 1206

def find_region(grid, region, i, j, view):
    view.add((i, j))
    region[-1].append([i, j])
    for a, b in cross:
        if cvnpgrid(grid, i+a, j+b, grid[i][j]) and (i+a, j+b) not in view:
            find_region(grid, region, i+a, j+b, view)


"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    t = 0
    view = set()
    region = []
    grid, _ = npgrid(lines, str)
    for i, j in enpgrid(grid):
        if (i, j) not in view:
            region.append([])
            find_region(grid, region, i, j, view)

    for r in region:
        f = 0
        fences = set()
        for i, j in r:
            for a, b in cross:
                if [i+a,j+b] not in r:
                    fences.add((i, j, a,b))
                    x, y = d_tr(a, b)
                    if (i+x, j+y, a, b) not in fences and (i-x, j-y, a, b) not in fences:
                        f += 1
                    c = 1
                    while [i+x*c,j+y*c] in r and [i+x*c+a,j+y*c+b] not in r:
                        fences.add((i+x*c, j+y*c, a, b))
                        c += 1
                    c = 1
                    while [i-x*c,j-y*c] in r and [i-x*c+a,j-y*c+b] not in r:
                        fences.add((i-x*c, j-y*c, a, b))
                        c += 1
        t += f * len(r)
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
    b, current, ref, ignored = main("ref")
    if ignored:
        print(f"--> Ref was ignored ⭕\n")
    elif b:
        print(f"\n--> Ref is valid ✅ : expected \033[1m{ref}\033[0m, get \033[1m{current}\033[0m\n")
    else:
        print(f"\n--> Ref is not valid ❌ : expected \033[1m{ref}\033[0m (type: {type(ref)}), get \033[1m{current}\033[0m (type: {type(current)})")
        print("Killed")
        exit(0)
    b, current, ref, ignored  = main("input")
    if b:
        print(f"--> Result is \033[1m{current}\033[0m")
        pyperclip.copy(current)