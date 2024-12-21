from collections import deque

keypad = {
    '7' : (0, 0),
    '8' : (0, 1),
    '9' : (0, 2),
    '4' : (1, 0),
    '5' : (1, 1),
    '6' : (1, 2),
    '1' : (2, 0),
    '2' : (2, 1),
    '3' : (2, 2),
    '0' : (3, 1),
    'A' : (3, 2),
}

keypad_inaccessible = (3, 0)

d_keypad = {
    '^' : (0, 1),
    'A' : (0, 2),
    '<' : (1, 0),
    'v' : (1, 1),
    '>' : (1, 2),
}

d_keypad_inaccessible = (0, 0)

dir_to_sym = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, 1): '>',
    (0,-1): '<',
}

cache = {}

def get_all_possibilities(cur, new_cur, pad_inaccessible):
    poss = []
    ej, ei = new_cur
    m = 0
    q = deque([(cur[0], cur[1], 0)])
    while q:
        j, i, p = q.popleft()
        while len(poss) <= p:
            poss.append([])
        f = 0
        if (j, i) == new_cur:
            poss[p].append('A')
            continue
        copy = poss[p].copy()
        if j > ej and (j - 1, i) != pad_inaccessible:
            poss[p].append(dir_to_sym[(-1, 0)])
            q.append((j - 1, i, p))
            f = 1
        elif j < ej and (j + 1, i) != pad_inaccessible:
            if f:
                poss.append([])
                p = m + 1
                for co in copy:
                    poss[p].append(co)
                m += 1
            f = 1
            poss[p].append(dir_to_sym[(1, 0)])
            q.append((j + 1, i, p))

        if i < ei and (j, i + 1) != pad_inaccessible:
            if f:
                poss.append([])
                p = m + 1
                for co in copy:
                    poss[p].append(co)
                m += 1
            poss[p].append(dir_to_sym[(0, 1)])
            q.append((j, i + 1, p))
        elif i > ei and (j, i - 1) != pad_inaccessible:
            if f:
                poss.append([])
                p = m + 1
                for co in copy:
                    poss[p].append(co)
                m += 1
            poss[p].append(dir_to_sym[(0, -1)])
            q.append((j, i - 1, p))
    return poss

def get_complexity_write(c, cur, pad, pad_inaccessible, d):
    if (c, cur, d) in cache:
        return cache[(c, cur, d)]

    new_cur = pad[c]

    poss = get_all_possibilities(cur, new_cur, pad_inaccessible)

    if d != 0:
        s = []
        for p in poss:
            ml = []
            p_cur = d_keypad['A']
            for e in p:
                p_cur, mll = get_complexity_write(e, p_cur, d_keypad, d_keypad_inaccessible, d-1)
                ml.append(mll)
            s.append(sum(ml))
        cache[(c, cur, d)] = new_cur, min(s)
        return new_cur, min(s)
    else:
        complexity = min([len(p) for p in poss])
        cache[(c, cur, d)] = new_cur, complexity
        return new_cur, complexity

"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    s = 0
    for code in lines:
        cur = keypad['A']
        complexity = 0
        for c in code:
            cur, com = get_complexity_write(c, cur, keypad, keypad_inaccessible, 25)
            complexity += com
        s += complexity * int(code[:len(code)-1])
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