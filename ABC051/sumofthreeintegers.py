K, S = [int(n) for n in input().split()]

count = 0

for x in range(min(S, K)+1):
    for y in range(x+1):
        z = S - x - y
        if z <= y and z >= 0:
            num_distinct = len({x,y,z})
            if num_distinct == 1:
                count += 1
            if num_distinct == 2:
                count += 3
            if num_distinct == 3:
                count += 6

print(count)