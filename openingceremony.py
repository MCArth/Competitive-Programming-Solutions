import sys
i=0
for x in sys.stdin:
    if i==0:
        numOfBuildings = int(x.rstrip())
        i+=1
    else:
        buildings = [int(a) for a in x.rstrip().split()]

numOfSideways=0
totalCharges=0
buildings.sort()

goneOver=0
for height in buildings:
    while height-numOfSideways>0:
        if buildings[len(buildings)-1]-numOfSideways >= numOfBuildings:
            numOfBuildings-=1
            totalCharges+=1
            buildings.pop()
            if len(buildings)==goneOver:
                break

        else:
            numOfSideways+=1
            totalCharges+=1

    numOfBuildings-=1
    goneOver+=1


print(totalCharges)
