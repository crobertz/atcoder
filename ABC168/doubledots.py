N, M = [int(n) for n in input().split()]

# node:connected
graph = {node:set() for node in range(1,N+1)}

for _ in range(M):
    A, B = [int(n) for n in input().split()]
    graph[A].add(B)
    graph[B].add(A)

to_visit = set(range(2,N+1))
level = 0

posts = {}

while to_visit:
    # base
    if level == 0:
        levels = {0:{1:None}}
        current_level = {1}
    
    # loop
    else:
        prevs = levels[level-1]
        levels[level] = {}
        for prev in prevs:
            for nbr in graph[prev]:
                if nbr in to_visit:
                    levels[level][nbr] = prev
                    posts[nbr] = prev
                    to_visit.remove(nbr) 
    
    level += 1

print('Yes')
for i in range(2,N+1):
    print(posts[i])