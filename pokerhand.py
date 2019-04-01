hand = input().rstrip().split()

ranks = {}


for i in range(len(hand)):
    ranks[hand[i][0]] = ranks.get(hand[i][0], 0)+1

maxThing = 0
for x in ranks:
    if ranks[x] > maxThing:
        maxThing = ranks[x]
print(maxThing)
