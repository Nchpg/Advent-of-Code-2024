def cost(M):
    s = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'O':
                s+=(len(M)-i)
    return s

def nord(M):
    for i in range(1, len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'O':
                k = 1
                while i-k >= 0 and M[i-k][j] == '.':
                    M[i-k+1][j] = '.'
                    M[i-k][j] = 'O'
                    k+=1
    return M


with open("input.txt") as f:
    lines = [line.strip() for line in f]
    M = []
    for l in lines:
        M.append(list(l))
    M = nord(M)

print("[DAY14-1] Answer is", cost(M))