N, K = tuple(int(n) for n in input().split())

count = 0
while N > 0:
    N = N // K
    count += 1

print(count)
