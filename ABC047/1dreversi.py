S = input()

def countcomponents(S):
    count = 1
    current = S[0]
    for i in range(len(S)):
        if S[i] != current:
            count += 1
            current = S[i]
    return count

print(countcomponents(S) - 1)