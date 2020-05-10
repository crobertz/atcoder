x1, y1, r = [int(n) for n in input().split()]
x2, y2, x3, y3 = [int(n) for n in input().split()]

def sqdist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

if x1 - x2 >= r and x3 - x1 >= r and y3 - y1 >= r and y1 - y2 >= r:
    print('NO')
else:
    print('YES')
if sqdist(x1,y1,x2,y2) <= r**2 and sqdist(x1,y1,x3,y3) <= r**2 and sqdist(x1,y1,x2,y3) <= r**2 and sqdist(x1,y1,x3,y2) <= r**2:
    print('NO')
else:
    print('YES')