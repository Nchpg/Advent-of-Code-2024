from collections import defaultdict
from AOC2024.aoc_tools import *

def compute_next(sn):
    res = sn * 64
    sn = sn^res
    sn = sn % 16777216

    res = sn // 32
    sn = sn^res
    sn = sn % 16777216

    res = sn * 2048
    sn = sn^res
    sn = sn % 16777216
    return sn


"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):

    number = pll(lines, t=int)

    #compute in advance last digit sequences
    last_nb = []
    for l in number:
        sn = l[0]
        p = sn % 10
        last_nb.append([p])
        for _ in range(1999):
            sn = compute_next(sn)
            p = sn % 10
            last_nb[-1].append(p)

    #group sequence in dict with associated index and last_digit
    L = defaultdict(dict)
    for j in range(len(number)):
        S = []
        for k in range(1, len(last_nb[j])):
            S.append(last_nb[j][k] - last_nb[j][k-1])
            while len(S) > 4:
                del S[0]
            if len(S) == 4:
                if not L[(tuple(S))].get(j):
                    L[(tuple(S))][j] = last_nb[j][k]

    #compute the sequence that give the max bananas
    s = 0
    for k, v in L.items():
        s = max(s, sum([v[ind] for ind in v]))
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