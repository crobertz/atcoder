N, K = [int(n) for n in input().split()]

sunuke = set()
for _ in range(K):
    _ = input()
    A = input().split()
    for a in A:
        sunuke.add(a)

print(N - len(sunuke))