N, K = [int(n) for n in input().split()]
#dice = [int(n) for n in input().split()]
evs = [(1 + int(n))/2 for n in input().split()]
cumsum = [0]

for i in range(1,N+1):
    cumsum.append(cumsum[i-1] + evs[i-1])

k_cum = [cumsum[i+K] - cumsum[i] for i in range(N-K+1)]

print(max(k_cum))