N, M = [int(n) for n in input().split()]

# node:connected
graph = {node:set() for node in range(1,N+1)}

for _ in range(M):
    A, B = [int(n) for n in input().split()]
    graph[A].add(B)
    graph[B].add(A)

to_visit = set(range(2,N+1))
current_level = {1}
to_visit = to_visit - current_level
level = 0
levels = {0:{1}}
seen = {1}

while to_visit:
    level += 1
    next_level = set()
    for i in current_level:
        next_level = next_level.union(graph[i] & to_visit)
    
    levels[level] = next_level    
    current_level = next_level
    to_visit = to_visit - current_level

prevs = {}
for level in reversed(range(1,len(levels))):
    for node in levels[level]:
        prevs[node] = set()
        for nbr in graph[node]:
            if nbr in levels[level-1]:
                prevs[node].add(nbr)

# print(prevs)

posts = {1:1}

for level in range(1,len(levels)):
    for node in levels[level]:
        for prev in prevs[node]:
            if prev in posts:
                posts[node] = prev
                break

# print(posts)

for i in range(2, N+1):
    print(posts[i])