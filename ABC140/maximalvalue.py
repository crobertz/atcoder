N = int(input())
B = [int(n) for n in input().split()]

total = B[0] + B[-1]
for i in range(N-2):
    total += min(B[i], B[i+1])

print(total)