import math

k = int(input())

total = 0
for a in range(1,k+1):
    for b in range(a,k+1):
        for c in range(b,k+1):
            abc = {a,b,c}
            div = 1
            if len(abc) == 2:
                div = 3
            elif len(abc) == 1:
                div = 1
            elif len(abc) == 3:
                div = 6
            #print(str(a) + " " + str(b) + " " + str(c))
            add = div * math.gcd(math.gcd(a,b),c)
            #print(len(abc))
            #print(div)
            #print(add)
            total += add

print(total)
