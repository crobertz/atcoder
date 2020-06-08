N, K = [int(n) for n in input().split()]

A = [1] + [int(n) for n in input().split()]

dest = []

current = 0
count = 0
next_dest = A[current]
seen = {}

while not next_dest in seen:
    current = next_dest
    next_dest = A[current]
    dest.append(current)
    seen[current] = count
    count += 1

cycle_start = seen[next_dest]
cycle_length = seen[current] - cycle_start + 1

if K <= cycle_start:
    print(dest[K])
else:
    print(dest[cycle_start + ((K - cycle_start) % cycle_length)])