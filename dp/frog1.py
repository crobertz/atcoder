N = int(input())

Heights = [int(n) for n in input().split()]
Costs = [-1 for n in range(N)]

for i in range(N):
    if i == 0:
        Costs[i] = 0
    elif i == 1:
        Costs[i] = abs(Heights[1] - Heights[0])
    else:
        Costs[i] = min(Costs[i-1] + abs(Heights[i] - Heights[i-1]), Costs[i-2] + abs(Heights[i] - Heights[i-2]))

print(Costs[-1])
