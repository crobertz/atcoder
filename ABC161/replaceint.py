list_input = [int(n) for n in input().split()]

N = list_input[0]
K = list_input[1]

while N > abs(N - K):
    if N >= K:
        N = N % K
    else:
        N = K - N
print(N)
