with open("input.txt", "r") as f:
    lines = f.readlines()
    s = 0
    for line in lines:

        line = line.strip()
        l = len(line)
        i = 0
        while i < l and (line[i] < '0' or line[i] > '9'):
            i+=1

        j = l-1
        while j >= 0 and (line[j] < '0' or line[j] > '9'):
            j -= 1
        s+= (ord(line[i])-ord('0'))*10+ord(line[j])-ord('0')
    print("[DAY1-1] Answer is", s)