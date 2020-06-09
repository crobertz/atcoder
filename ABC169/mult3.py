A, B = input().split()
A = int(A)
B = int(B[:-3])*100 + int(B[-2:])

print(A*B // 100)