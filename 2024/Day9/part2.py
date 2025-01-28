REF_RES = 2858

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):

    line = [int(x) for x in lines[0]]

    # CREATE LIST WITH '.' AND ID
    points = []
    id = 0
    for i, p in enumerate(line):
        if i % 2 == 0:
            for _ in range(p):
                points.append(id)
            id += 1
        else:
            for _ in range(p):
                points.append('.')

    # FREE SPACE LIST
    S = []
    for i in range(len(points)):
        if points[i] == '.':
            S[-1] = [S[-1][0] if S[-1][0] != -1 else i, S[-1][1]+1]
        elif len(S) == 0 or S[-1][0] != -1:
            S.append([-1, 0])


    # MOVE FILE
    rea = points.copy()
    l = len(rea)
    j = l - 1
    while j >= 0:
        c = 0
        while rea[j - c] == rea[j]:
            c += 1
        for b, (k, s) in enumerate(S):
            if s >= c and k < j:
                for a in range(c):
                    rea[j-c+1+a], rea[k+a] = rea[k+a], rea[j-c+1+a]
                S[b] = [k+c, s-c]
                break
        j -= c
        while rea[j] == '.':
            j -= 1

    # CHECKSUM
    t = 0
    for i, v in enumerate(rea):
        if v == '.': continue
        t +=i*v
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