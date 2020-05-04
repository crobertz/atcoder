A, B, C, D = [int(n) for n in input().split()]

counter = -1

while A > 0 and C > 0:
    counter += 1
    if counter % 2 == 0:
        C -= B
    else:
        A -= D

if counter % 2 == 0:
    print('Yes')
else:
    print('No')
