cache = {}

def rec(stone, depth):
    if depth >= 75:
        return 1
    if (stone, depth) in cache:
        return cache[(stone, depth)]
    if stone == 0:
        cache[(stone, depth)] = rec(1, depth + 1)
        return cache[(stone, depth)]
    elif len(str(stone)) % 2 == 0:
        li = int(str(stone)[:int(len(str(stone)) / 2)])
        ri = int(str(stone)[int(len(str(stone)) / 2):])
        l = rec(li, depth + 1)
        r = rec(ri, depth + 1)
        cache[(stone, depth)] = l + r
        return cache[(stone, depth)]
    cache[(stone, depth)] = rec(stone*2024, depth+1)
    return cache[stone, depth]



"""
START FUNCTION TO SOLVE THE PROBLEM
"""
def manager(lines):
    stones = [int(s) for s in lines[0].split()]
    t = 0
    for s in stones:
        t += rec(s, 0)
    return t




















"""
Below is a model to compare/launch the result with the expected one (not part of today's problem). 

The entry point of the problem is the manager function
"""
import sys
import pyperclip
sys.setrecursionlimit(10**6)


if __name__ == "__main__":
    pyperclip.copy("")
    with open("input", "r") as file:
        res = manager(file.read().splitlines())
        print(f"--> Result is \033[1m{res}\033[0m")
        pyperclip.copy(res)