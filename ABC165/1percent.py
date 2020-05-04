X = int(input())
amt = 100
year = 0
while amt < X:
    amt = int(amt * 1.01)
    year += 1
print(year)