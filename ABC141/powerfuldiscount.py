import heapq

N, M = [int(n) for n in input().split()]
A = [-int(n) for n in input().split()]
heapq.heapify(A)

while M > 0:
    M -= 1
    Amax = -heapq.heappop(A) // 2
    heapq.heappush(A, -Amax)

print(-sum(A))