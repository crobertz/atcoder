import sys

N, M = [int(n) for n in input().split()]

def factorial_mod(n):
    result = 1
    for i in range(1,n+1):
        result = (result * i) % (10**9 + 7)
    return result

if abs(N - M) > 1:
    print(0)
    sys.exit(0)

N_fact = factorial_mod(N)
M_fact = factorial_mod(M)

if N == M:
    print((2*N_fact*M_fact) % (10**9 + 7))
else:
    print((N_fact*M_fact) % (10**9 + 7))