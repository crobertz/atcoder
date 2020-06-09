import math

a, b, x = [int(n) for n in input().split()]

def to_deg(theta):
    return theta * 180 / math.pi

if x <= a**2 * b / 2:
    theta = math.atan((a * b**2) / (2*x))
else:
    theta = math.atan(2 * (a**2 * b - x) / a**3)

print(to_deg(theta))