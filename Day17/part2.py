from AOC2024.aoc_tools import *

#REF_RES = 117440


def i0(b, R):
    C = [0, 1, 2, 3, R['A'], R['B'], R['C']]
    n = R['A']
    d = pow(2, C[b])
    R['A'] = n//d

def i1(b, R):
    R['B'] = b ^ R['B']

def i2(b, R):
    C = [0, 1, 2, 3, R['A'], R['B'], R['C']]
    R['B'] = C[b]%8

def i3(b, R, PC):
    if R['A'] == 0:
        return PC
    PC = b//2 - 1
    return PC

def i4(b, R):
    R['B'] = R['B']^R['C']

def i5(b, R, has_print, P):
    C = [0, 1, 2, 3, R['A'], R['B'], R['C']]
    if has_print:
        P+=","
    P += str(C[b] % 8)
    has_print = 1
    return has_print, P

def i6(b, R):
    C = [0, 1, 2, 3, R['A'], R['B'], R['C']]
    n = R['A']
    d = pow(2, C[b])
    R['B'] = n//d

def i7(b, R):
    C = [0, 1, 2, 3, R['A'], R['B'], R['C']]
    n = R['A']
    d = pow(2, C[b])
    R['C'] = n//d

def run(R, I, Ref):
    P = ""
    PC = 0
    has_print = 0
    while PC < len(I):
        a, b = I[PC]
        if a == 0:
            i0(b, R)
        elif a == 1:
            i1(b, R)
        elif a == 2:
            i2(b, R)
        elif a == 3:
            PC = i3(b, R, PC)
        elif a == 4:
            i4(b, R)
        elif a == 5:
            has_print, P = i5(b, R, has_print, P)
            if len(P) > len(Ref):
                print("Impossible")
                break
        elif a == 6:
            i6(b, R)
        elif a == 7:
            i7(b, R)
        PC += 1
    return P


"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    lines = change_line_delim(lines, "\n\n")
    R = nums(lines[0])
    R = {'A': R[0], 'B': R[1], 'C': R[2]}
    Ref = lines[1].split(" ")[-1]
    I = nums(lines[1].split(" ")[-1])
    I = [(I[2*i], I[2*i+1]) for i in range(len(I)//2)]
    c = pow(8, 2*len(I)-1)
    nb = 0
    while True:
        if c > pow(8, 2*len(I)):
            print("Error not found")
            break
        R['A'] = c
        P = run(R, I, Ref)
        print("Has : ", P, "\t\tExpected : ", Ref)
        if P == Ref:
            print("Iteration number", nb)
            return c
        j = len(P)-1
        i = 2*len(I) - 1
        while j >= 0:
            if P[j] != Ref[j]:
                o = pow(8, i)
                break
            j -= 2
            i -= 1
        c += o
        nb+=1

    return 0
























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