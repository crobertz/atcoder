import sys

row1 = [int(n) for n in input().split()]
row2 = [int(n) for n in input().split()]
row3 = [int(n) for n in input().split()]

card = [row1,row2,row3]

#print(card)

N = int(input())
for n in range(N):
    bn = int(input())
    for i in range(len(card)):
        for j in range(len(card)):
            if card[i][j] == bn:
                card[i][j] = 0

#print(card)

for i in range(len(card)):
    check_i = 0
    for j in range(len(card)):
        check_i += card[i][j]
    #print('check_i: ' + str(check_i))
    if check_i == 0:
        print('Yes')
        sys.exit(0)
for j in range(len(card)):
    check_j = 0
    for i in range(len(card)):
        check_j += card[i][j]
    #print("check_j: " + str(check_j))
    if check_j == 0:
        print('Yes')
        sys.exit(0)

check_diag1 = 0
check_diag2 = 0
for i in range(len(card)):
    check_diag1 += card[i][i]
    check_diag2 += card[len(card)-i-1][i]
#print('check_diag1: ' + str(check_diag1))
#print('check_diag2: ' + str(check_diag2))
if check_diag1 == 0 or check_diag2 == 0:
    print('Yes')
    sys.exit(0)

print('No')
