REF_RES = 18


def check(L, i, j, c):
    return 0 <= i < len(L) and 0 <= j < len(L[i]) and c == L[i][j]

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    t = 0
    L = []
    for line in lines:
        l = line.strip()
        L.append([])
        for c in l:
            L[-1].append(c)
    for i in range(len(L)):
        for j in range(len(L[i])):
            if check(L, i, j, 'X'):
                for s in [-1, 1]:
                    if check(L, i, j+1*s, 'M') and check(L, i, j+2*s, 'A') and check(L, i, j+3*s, 'S'):
                        t += 1
                    if check(L, i+1*s, j, 'M') and check(L, i+2*s, j, 'A') and check(L, i+3*s, j, 'S'):
                        t += 1
                    if check(L, i+1*s, j+1*s, 'M') and check(L, i+2*s, j+2*s, 'A') and check(L, i+3*s, j+3*s, 'S'):
                        t += 1
                    if check(L, i+1*s, j-1*s, 'M') and check(L, i+2*s, j-2*s, 'A') and check(L, i+3*s, j-3*s, 'S'):
                        t += 1
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
