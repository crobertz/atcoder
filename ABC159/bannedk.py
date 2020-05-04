N = int(input())
As = [int(n) for n in input().split()]

vals = {}
for A in As:
    if A in vals:
        vals[A] += 1
    else:
        vals[A] = 1

#print(vals)

choose2 = {}
for val in vals:
    num = vals[val]
    choose2[val] = num*(num - 1) // 2

#print(choose2)

total = 0
for k in choose2:
    total += choose2[k]
#print("total: " + str(total))

for Ak in As:
    print(total - (vals[Ak] - 1))
