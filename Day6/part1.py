from AOC2024.aoc_tools import *

REF_RES = 41

def turn_right(dx, dy):
    if (dx, dy) == (-1, 0):
        return 0, 1
    if (dx, dy) == (0, 1):
        return 1, 0
    if (dx, dy) == (1, 0):
        return 0, -1
    if (dx, dy) == (0, -1):
        return -1, 0


def process(g, x, y, w, h):
    v = set()
    dx, dy = -1, 0
    g_cpy = g.copy()
    while 0 <= x < w and 0 <= y < h:
        v.add((x, y, dx, dy))
        if not (0 <= x + dx < w and 0 <= y + dy < h):
            return 0
        while g_cpy[x + dx][y + dy] in '#O':
            dx, dy = d_tr(dx, dy)
        x, y = x + dx, y + dy

        if (x, y, dx, dy) in v:
            return 1
    return 0

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    g, _ = npgrid(lines, str)

    xs, ys = fnpgrid(g, '^')

    dx, dy = -1, 0
    g_path = g.copy()
    x, y = xs, ys
    view = set()
    while cnpgrid(g, x, y):
        view.add((x,y))
        if not cnpgrid(g, x+dx, y+dy):
            break
        while g_path[x + dx][y + dy] == '#':
            dx, dy = d_tr(dx, dy)
        x, y = x + dx, y + dy

    return len(view)























"""
Below is a model to compare the result with the expected one (not part of today's problem). 

The entry point of the problem is the manager function
"""
import pyperclip
import ast
import sys
import time
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
        s = time.time()
        res = manager(lines)
        print(f"[{round(time.time() - s, 2)}] sec")
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
        print(f"\n--> Ref is valid ✅ : excpeted \033[1m{ref}\033[0m, get \033[1m{current}\033[0m\n")
    else:
        print(f"\n--> Ref is not valid ❌ : excpeted \033[1m{ref}\033[0m (type: {type(ref)}), get \033[1m{current}\033[0m (type: {type(current)})")
        print("Killed")
        exit(0)
    b, current, ref, ignored  = main("input")
    if b:
        print(f"--> Result is \033[1m{current}\033[0m")
        pyperclip.copy(current)