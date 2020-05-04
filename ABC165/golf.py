import sys

K = int(input())
A, B = [int(n) for n in input().split()]

for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        sys.exit(0)
print('NG')