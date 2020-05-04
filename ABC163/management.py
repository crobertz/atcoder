N = int(input())
As = [int(n) for n in input().split()]

dict = {}
for i in range(1,N+1):
    dict[i] = 0

for A in As:
    dict[A] += 1

for i in range(1,N+1):
    print(dict[i])
