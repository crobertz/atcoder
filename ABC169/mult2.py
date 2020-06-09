import sys

N = int(input())

As = [int(n) for n in input().split()]
As_set = set(As)

limit = 10**18

prod = 1

if 0 in As_set:
    print(0)
    sys.exit(0)

over = False
for A in As:
    prod *= A
    if prod > limit:
        print(-1)
        sys.exit(0)

print(prod)