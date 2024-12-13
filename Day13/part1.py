import numpy as np

from AOC2024.aoc_tools import *

REF_RES = 480

def compute(A, B, T):
    L = np.array([A, B]).transpose()
    Y = np.array([T]).transpose()
    X = linear_solve(L, Y).transpose()
    x, y = [round(e) for e in X[0]]
    if x  > 100 or y > 100:
        return 0
    if A[0] * x + B[0] * y == T[0] and A[1] * x + B[1] * y == T[1]:
        return 3 * x + y
    return 0

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    t = 0
    A = []
    B = []
    T = []
    i = 0
    for line in lines:
        if line == "":
            t += compute(A, B, T)
            i = 0
            continue
        if i == 0:
            R = re.findall("X\+(\d+), Y\+(\d+)", line)
            A = [int(R[0][0]), int(R[0][1])]
            i += 1
        elif i == 1:
            R = re.findall("X\+(\d+), Y\+(\d+)", line)
            B = [int(R[0][0]), int(R[0][1])]
            i += 1
        elif i == 2:
            R = re.findall("X=(\d+), Y=(\d+)", line)
            T = [int(R[0][0]), int(R[0][1])]
            i += 1
    t += compute(A, B, T)
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
    _, current, _, _  = main("input")
    if b:
        print(f"--> Result is \033[1m{current}\033[0m")
        pyperclip.copy(current)