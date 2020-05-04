# TLE in python; AC in pypy

N, K = [int(n) for n in input().split()]

Heights = [int(n) for n in input().split()]
Costs = [float('inf') for n in range(N)]

for i in range(N):
    if i == 0:
        Costs[i] = 0
    elif i < K:
        for j in range(i+1):
            Costs[i] = min(Costs[i], Costs[i-j] + abs(Heights[i] - Heights[i-j]))
    else:
        #Costs[i] = min(Costs[i-1] + abs(Heights[i] - Heights[i-1]), Costs[i-2] + abs(Heights[i] - Heights[i-2]))
        for j in range(K+1):
            Costs[i] = min(Costs[i], Costs[i-j] + abs(Heights[i] - Heights[i-j]))

print(Costs[-1])
