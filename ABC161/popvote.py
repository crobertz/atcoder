n_m = [int(n) for n in input().split()]
N = n_m[0]
M = n_m[1]

votes = [int(n) for n in input().split()]

total_votes = sum(votes)
thresh = total_votes / (4 * M) #better with mult?

count = 0

for A in votes:
    if 4*M*A >= total_votes:
        count += 1
    if count >= M:
        print('Yes')
        break

if count < M:
    print('No')
