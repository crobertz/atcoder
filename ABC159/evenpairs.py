input_lst = [int(n) for n in input().split()]

N = input_lst[0]
M = input_lst[1]

print((N*(N-1) + M*(M-1)) // 2)
