from collections import deque

from AOC2024.aoc_tools import *

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    init_wires, connections = change_line_delim(lines, "\n\n")
    init_wires = init_wires.split("\n")
    connections = connections.split("\n")
    seen = {}


    for wire in init_wires:
        name, value = wire.split(": ")
        seen[name] = int(value)

    q = deque([])
    for con in connections:
        (i1, b, i2), o = con.split(" -> ")[0].split(" "), con.split(" -> ")[1]
        q.append((i1, b, i2, o))

    while q:
        i1, b, i2, o = q.popleft()
        if i1 not in seen.keys() or i2 not in seen.keys():
            q.append((i1, b, i2, o))
            continue
        if b == "AND":
            seen[o] = seen[i1] & seen[i2]
        elif b == "OR":
            seen[o] = seen[i1] | seen[i2]
        elif b == "XOR":
            seen[o] = seen[i1] ^ seen[i2]
        else:
            print("NOT GOOD BITWISE OPERATOR\n")
            exit(1)


    z = 0
    for k, v in seen.items():
        if k[0] == "z":
            i = int(k[1:])
            z = z | (v<<i)

    return z
























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