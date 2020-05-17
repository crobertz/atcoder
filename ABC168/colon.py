import math

A, B, H, M = [int(n) for n in input().split()]

theta_H = (math.pi / 6)*(H + M/60)
theta_M = (math.pi/30)*M

def to_rect(r,theta):
    return (r*math.cos(theta), r*math.sin(theta))

def dist(tuple1,tuple2):
    return math.sqrt((tuple1[0] - tuple2[0])**2 + (tuple1[1] - tuple2[1])**2)

print(dist(to_rect(A,theta_H), to_rect(B,theta_M)))