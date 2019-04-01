from sys import stdin
waste = input()
bands = []
inBands = True
first = True
friends = []

for x in stdin:
    if inBands:
        x = x.rstrip().split()
        if len(x) == 2:
            if len(bands) == 0:
                bands.append((float(x[0]), float(x[1])*0.01))
            else:
                bands.append((float(x[0])+bands[-1][0], float(x[1])*0.01))
        else:
            inBands = False
            upperBand = float(x[0])*0.01

    else:
        if first:
            first = False
        else:
            friends.append([float(a) for a in x.rstrip().split()])


for x in friends:
    firstBand = len(bands)
    currMoney = x[0]
    totNeeded = x[1]
    total = 0
    lotTotal = 0
    for i in range(len(bands)):
        if currMoney < bands[i][0]:
            firstBand = i
            break
        
    i = firstBand

    while i < len(bands):
        needed = totNeeded - lotTotal
        percBand = bands[i][1]

        if 1-percBand == 0:
            total += bands[i][0]-currMoney
            currMoney = bands[i][0]
            i += 1

        elif needed*(1/(1-percBand)) > bands[i][0]-currMoney:
            lotTotal += (bands[i][0]-currMoney)*(1-percBand)
            total += bands[i][0]-currMoney
            currMoney = bands[i][0]
            i += 1

        else:
            lotTotal += needed
            total += needed*(1/(1-percBand))
            break

    total += (totNeeded-lotTotal)*(1/(1-upperBand))

    print(total)



