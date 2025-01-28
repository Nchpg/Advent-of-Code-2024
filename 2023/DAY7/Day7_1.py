def get_type(a):
    s = {}
    for c in a:
        if not c in s:
            s[c] = 1
        else:
            s[c] +=1
    if len(s) == 1:
        return 1
    if len(s) == 2:
        for c in s:
            if s[c] in [1,4]:
                return 2
            else:
                return 3
    if len(s) == 3:
        for c in s:
            if s[c] == 3:
                return 4
        return 5
    if len(s) == 4:
        return 6
    if len(s) == 5:
        return 7

def get_val(c):
    if c == "A":
        return 14
    if c == "K":
        return 13
    if c == "Q":
        return 12
    if c == "J":
        return 11
    if c == "T":
        return 10
    return ord(c)-ord('0')




def is_greater(a, b):
    if get_type(a) < get_type(b):
        return True
    elif get_type(a) > get_type(b):
        return False
    for c, d in zip(a, b):
        if get_val(c) < get_val(d):
            return False
        elif get_val(c) > get_val(d):
            return True

def sort(L):
    j = len(L)-1
    while j > 0 and is_greater(L[j], L[j-1]):
        L[j],L[j-1] = L[j-1],L[j]
        j-=1


T = {}
L = []
with open("input.txt") as f:
    lines = [ line.strip() for line in f ]
    for l in lines:
        m,g = l.split()
        T[m] = int(g)
        L.append(m)
        sort(L)

    _sum = 0
    mul = len(L)
    i = 0
    for k in L:
        _sum+=T[k]*(mul-i)
        i+=1

    print("[DAY7-1] Answer is", _sum)