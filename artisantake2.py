useless = input()
prices = [int(a) for a in input().rstrip().split()]

pricesUsed = [False]*1000000

total=0
for x in prices:
    if not pricesUsed[x-1]:
        total += x
        pricesUsed[x-1] = True
print(total)
