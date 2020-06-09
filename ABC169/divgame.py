import math
import itertools
import sys

N = int(input())
N_copy = N

if N == 1:
    print(0)
    sys.exit(0)


def prime_factors(n):
    # https://codereview.stackexchange.com/a/121869
    # i ranges over 2 and odd numbers 3, 5, 7, ...
    # returns each prime as many times as it divides n
    """Find prime factorization of n"""
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

primes = {}

for p in range(2, int(math.sqrt(N))+1):
    while N % p == 0:
        N //= p
        if p in primes:
            primes[p] += 1
        else:
            primes[p] = 1

def find_k(E):
    k = 1
    while k**2 + k <= 2*E:
        k += 1
    return k-1

total = 0

# for p in range(2, N+1):
#     E = 0
#     while N % p == 0:
#         N //= p
#         E += 1
#     total += find_k(E)

# print(total)

for p in primes:
    total += find_k(primes[p])


prod = 1
for p in primes:
    prod *= p ** primes[p]

# print(prod)

if prod != N_copy:
    print(total + 1)
else:
    print(total)

# print(primes)
# if not primes:
#     print(1)
# else:
#     print(total)