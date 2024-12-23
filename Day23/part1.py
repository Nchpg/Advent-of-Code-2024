from collections import defaultdict
import itertools
from AOC2024.aoc_tools import *



"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):

    l = [re.findall("([a-z]+)-([a-z]+)", line)[0] for line in lines]

    d = defaultdict(list)
    for (p1, p2) in l:
        d[p1].append(p2)
        d[p2].append(p1)

    seen = set()
    team = set()
    for k, v in d.items():
        u = set()
        for x in v:
            u.add(x)
        for p in v:
            if k in d[p]:
                v = set()
                for x in d[p]:
                    v.add(x)
                z = list(u.intersection(v))
                for i in range(len(z)):
                    if (z[i], k, p) not in seen:
                        team.add((z[i], k, p))
                        for a, b, c in itertools.permutations([z[i], k, p]):
                            seen.add((a, b, c))

    s = 0
    for a, b, c in team:
        if a[0] == 't' or b[0] == 't' or c[0] == 't':
            s += 1

    return s
























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