N, M = [int(n) for n in input().split()]
heights = [int(n) for n in input().split()]

graph = {n:set() for n in range(1,N+1)}
for _ in range(M):
    A, B = [int(n) for n in input().split()]
    graph[A].add(B)
    graph[B].add(A)

total = 0
for node in graph:
    if graph[node] == None:
        total += 1
    else:
        better = True
        for nbr in graph[node]:
            if heights[nbr-1] >= heights[node-1]:
                better = False
                break
        if better:
            total += 1

print(total)
        