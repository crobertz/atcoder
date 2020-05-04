N = int(input())
#A = [int(n) for n in input().split()]

diff = set()
for i in range(1, N+1):
    for j in range(i+1, N+1):
        diff.add(j-i)

print(len(diff))