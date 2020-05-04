N = int(input())

X_list = [int(n) for n in input().split()]
total = 0
for X in X_list:
    total += X

avg_left = total // N
avg_right = (total // N) + 1

dist_left = 0
dist_right = 0
for X in X_list:
    dist_left += (X - avg_left)**2
    dist_right += (X - avg_right)**2

print(min(dist_left,dist_right))
