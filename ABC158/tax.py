import sys

A, B = tuple(int(n) for n in input().split())

for q in range(0,10):
    p = 10*B + q
    if int(p * 0.08) == A:
        print(p)
        sys.exit(0)

print(-1)
