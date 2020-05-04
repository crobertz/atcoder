import itertools
N, M, Q = [int(n) for n in input().split()]
data = [[int(n) for n  in input().split()] for _ in range(Q)]

As = itertools.combinations_with_replacement(range(1, M+1),N)

max_val = 0
for A in As:
    val = 0
    for abcd in data:
        if A[abcd[1]-1] - A[abcd[0]-1] == abcd[2]:
            val += abcd[3]
    if val > max_val:
        max_val = val

print(max_val)