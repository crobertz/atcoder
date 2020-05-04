from collections import deque

S = input()
Q = int(input())

q = deque(S)

parity = 0
for i in range(Q):
    T = input().split()
    if len(T) == 1:
        parity = (parity + 1) % 2
        #q.reverse()
    else:
        F = int(T[1])
        C = T[2]

        if parity == 0:
            if F == 1:
                q.appendleft(C)
            else:
                q.append(C)
        else:
            if F == 1:
                q.append(C)
            else:
                q.appendleft(C)

if parity == 1:
    q.reverse()

print(''.join(q))
