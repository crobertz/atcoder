A, B, C, K = [int(n) for n in input().split()]

if K <= A:
    print(K)
elif K <= A + B:
    print(A)
else:
    print(A - (K - (A + B)))