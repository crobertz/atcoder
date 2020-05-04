circum_total = [int(n) for n in input().split()]

circum = circum_total[0]
total = circum_total[1]

distances = [int(n) for n in input().split()]

mindist = circum
for index in range(len(distances)):
    if index == len(distances) - 1:
        rightdist = distances[0] + circum - distances[index]
    else:
        rightdist = distances[index+1] - distances[index]
    if index == 0:
        leftdist = distances[index] - distances[index-1] + circum
    else:
        leftdist = distances[index] - distances[index-1]
    maxdist = max(rightdist,leftdist)
    mindist = min(mindist, circum - maxdist)

print(mindist)
