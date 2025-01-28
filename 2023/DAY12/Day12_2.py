from functools import cache

@cache
def all_poss(a, b):
    if not b:
        # if remain # return 0 else 1
        return "#" not in a

    # curr = A
    # rest = B, C, D, ... Z
    # between each rest (and curr) at least 1 "."
    # max_space_possible = len(a) - A - 1 - B - 1 - C - 1 ... - Z = len(a) - sum(b) - len(b) + 1 (before) + 1 (after)

    max_space_possible = len(a) - sum(b) - len(b) + 2

    curr, rest = b[0], b[1:]
    res = 0

    # space increase --> -->  --> max:max_space_possible
    # len = space | len = current | next ; len = 1       | next + 1 (recursive call)
    # (no #)      | (no .)        | (no #  => next != #)
    for space in range(max_space_possible):
        next = curr+space

        # Check if in the space zone there is #. If # in space zone break the loop
        # Or check if next is out of range
        if "#" in a[:space] or next-1 == len(a):
            break

        # Check if in the current zone there is no ".". Skip if "." in current zone or if juste after current zone there is a #.
        if '.' not in a[space : next] and (next == len(a) or a[next] != "#"):
            res += all_poss(a[next+1:], rest)
    return res

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    s = 0
    i = 0
    for l in lines:
        a,b = l.split()
        b = b.split(",")
        for i, e in enumerate(b):
            b[i] = int(e)
        b = tuple(b)
        x = all_poss("?".join([a] * 5), b * 5)
        s += x
        i+=1

    print("[DAY12-2] Answer is", s)