N, M = tuple(int(n) for n in input().split())

As = [int(n) for n in input().split()]

for A in As:
    N -= A

print(max(N, -1))
