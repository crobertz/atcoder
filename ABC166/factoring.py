import sys
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
    X = int(input())
    divisors = factors(X)
    A = 0
    while True:
        for d in divisors:
            B = A - d
            check1 = A**5 - B**5
            check2 = -check1
            if check1 == X:
                print('{} {}'.format(A, B))
                sys.exit(0)
            if check2 == X:
                print('{} {}'.format(B, A))
                sys.exit(0)
        A += 1
            


if __name__ == "__main__":
    main()