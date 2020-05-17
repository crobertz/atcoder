import math

N = int(input())

def factortwo(N):
    factors = []
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            factors.append((i, N // i))
    return factors

print(sum(factortwo(N)[-1]) - 2)