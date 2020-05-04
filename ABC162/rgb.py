N = int(input())
S = input()

r = 0
g = 0
b = 0

for i in range(N):
    if S[i] == 'R':
        r += 1
    if S[i] == 'G':
        g += 1
    if S[i] == 'B':
        b += 1

rgb_tot = r*g*b
#print(rgb_tot)

for i in range(N):
    first = S[i]
    for j in range(i,N):
        if 2*j - i < N:
            if first != S[j] and first != S[2*j-i] and S[j] != S[2*j-i]:
                #print("%d %d %d" % (i,j,2*j-i))
                #print(rgb_tot)
                rgb_tot -= 1

print(rgb_tot)
