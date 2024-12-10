REF_RES = 123

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    t = 0
    pages = []
    order = []
    space = 0
    for line in lines:
        l = line.strip()
        if space == 1:
            x = l.split(',')
            order.append([])
            for y in x:
                order[-1].append(int(y))

        if l != '' and space == 0:
            a, b = l.split('|')
            pages.append([int(a), int(b)])
        else:
            space = 1


    bad = []
    for o in order:
        c = []
        v = []
        good = True
        for p in pages:
            if p[0] in o and p[1] in o:
                c.append(p)
        for x in o:
            for p in pages:
                if p[0] in o and p[1] == x and p[0] not in v:
                    good = False
                    break
            if not good:
                break
            v.append(x)
        if not good:
            bad.append(o)

    i = 0
    final = []
    for o in bad:
        good = False

        while not good:

            c = []
            v = []
            good = True
            for p in pages:
                if p[0] in o and p[1] in o:
                    c.append(p)
            j = 0
            for x in o:
                for p in pages:
                    if p[0] in o and p[1] == x and p[0] not in v:
                        a, b = bad[i].index(p[0]), bad[i].index(p[1])
                        bad[i][a], bad[i][b] = bad[i][b], bad[i][a]
                        good = False
                        break
                if not good:
                    break
                v.append(x)
                j += 1
        if good:
            final.append(o)
            t += o[int(len(o) / 2)]
        i += 1
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