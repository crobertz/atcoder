import sys
N = input()
As = [int(n) for n in input().split()]

for A in As:
    if A % 2 == 0:
        if not(A % 3 == 0 or A % 5 == 0):
            print('DENIED')
            sys.exit(0)

print('APPROVED')
