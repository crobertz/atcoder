S = input()
N = len(S)
#print(N)

def checkpalin(s):
    if s == s[::-1]:
        return True
    else:
        return False

if checkpalin(S) and checkpalin(S[:(N-1)//2]) and checkpalin(S[(N+3)//2:-1]):
    print('Yes')
else:
    print('No')
