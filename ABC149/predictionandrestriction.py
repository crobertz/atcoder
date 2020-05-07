N, K = [int(n) for n in input().split()]
R, S, P = [int(n) for n in input().split()]
T = input()

scoredict = {'r':R, 's':S, 'p':P}
winning = {'r':'p', 's':'r', 'p':'s'}
loss = {'r':'s', 's':'p', 'p':'r'}

picks = []
score = 0
for i in range(N):
    current = T[i]
    pick = winning[current]
    if i - K >= 0 and pick == picks[i-K]:
        if i + K < N and current == winning[T[i + K]]:
            pick == loss[current]
        else:
            pick = current
    else:
        score += scoredict[pick]
    picks.append(pick)

print(score)