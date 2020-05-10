import numpy as np
import sys
from itertools import chain, combinations

N, M, X = [int(n) for n in input().split()]

matrix = np.zeros((N,M+1))
for i in range(N):
    matrix[i] = np.array([int(n) for n in input().split()])

def checkthresh(A, thresh):
    return all(i >= thresh for i in A)

if not checkthresh(np.sum(matrix[:,1:],axis=0), X):
    print(-1)
    sys.exit(0)

def powerset(n):
    """returns generator for powerset of {0,1,...,n-1}"""
    # chain r-combinations generator for r=0, 1,..., n
    return chain.from_iterable(combinations(range(n), r) for r in range(n+1))

cost = np.inf
for subset in powerset(N):
    sum_subset = np.zeros((1,M+1))
    for i in subset:
        sum_subset += matrix[i,:]
    sum_subset = sum_subset[0]
    if checkthresh(sum_subset[1:], X):
        cost = min(cost, sum_subset[0])

print(int(cost))
