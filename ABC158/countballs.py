N, A, B = tuple(int(n) for n in input().split())

blue = (N // (A+B)) * A + min(A,N % (A+B))
print(blue)
