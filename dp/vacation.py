N = int(input())

# kth entry: [max up to ak, bk, ck]
max_happiness = [[None] * 3 for _ in range(N)]

for k in range(N):
    if k == 0:
        max_happiness[k] = [int(n) for n in input().split()]
    else:
        ak, bk, ck = [int(n) for n in input().split()]

        a_opt, b_opt, c_opt = max_happiness[k-1]
        max_happiness[k][0] = ak + max(b_opt, c_opt)
        max_happiness[k][1] = bk + max(a_opt, c_opt)
        max_happiness[k][2] = ck + max(a_opt, b_opt)

print(max(max_happiness[-1]))
