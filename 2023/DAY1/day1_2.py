
def change_value(s, i):
    l = len(s)
    if i+5<=l:
        if line[i:i+5] == "eight":
            s2 = list(s)
            for j in range(5):
                s2[i+j] = '8'
            s = ''.join(s2)
            return s
        elif line[i:i+5] == "seven":
            s2 = list(s)
            for j in range(5):
                s2[i+j] = '7'
            s = ''.join(s2)
            return s

        elif line[i:i+5] == "three":
            s2 = list(s)
            for j in range(5):
                s2[i+j] = '3'
            s = ''.join(s2)
            return s
    if i+4<=l:
        if line[i:i+4] == "four":
            s2 = list(s)
            for j in range(4):
                s2[i+j] = '4'
            s = ''.join(s2)
            return s
        elif line[i:i+4] == "five":
            s2 = list(s)
            for j in range(4):
                s2[i+j] = '5'
            s = ''.join(s2)
            return s

        elif line[i:i+4] == "nine":
            s2 = list(s)
            for j in range(4):
                s2[i+j] = '9'
            s = ''.join(s2)
            return s
        elif line[i:i+4] == "zero":
            s2 = list(s)
            for j in range(4):
                s2[i+j] = '0'
            s = ''.join(s2)
            return s
    if i+3<=l:
        if line[i:i+3] == "one":
            s2 = list(s)
            for j in range(3):
                s2[i+j] = '1'
            s = ''.join(s2)
            return s
        elif line[i:i+3] == "two":
            s2 = list(s)
            for j in range(3):
                s2[i+j] = '2'
            s = ''.join(s2)
            return s
        elif line[i:i+3] == "six":
            s2 = list(s)
            for j in range(3):
                s2[i+j] = '6'
            s = ''.join(s2)
            return s

    return s

with open("input.txt", "r") as f:
    lines = f.readlines()
    s = 0
    for line in lines:

        line = line.strip().lower()
        l = len(line)
        i = 0
        while i < l:
            line = change_value(line, i)
            if line[i] < '0' or line[i] > '9':
                i+=1
            else:
                break

        j = l-1
        while j >= 0:
            line = change_value(line, j)
            if line[j] < '0' or line[j] > '9':
                j -= 1
            else:
                break
        s+= (ord(line[i])-ord('0'))*10+ord(line[j])-ord('0')

    print("[DAY1-2] Answer is", s)