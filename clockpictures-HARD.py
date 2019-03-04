# Solution to: https://open.kattis.com/problems/clockpictures

import sys
i=0
for x in sys.stdin:
    x=[int(a) for a in x.rstrip().split()]
    if i==0:
        pass
    elif i==1:
        clock1 = x

    elif i==2:
        clock2 = x
        
    i+=1


for a, b in zip([clock1, clock2], range(2)):
    numCount = [0] * 360000
    for num in a:
        numCount[num] += 1

    clock = []
    for index in range(len(numCount)):
        if numCount[index] != 0:
            for x in range(numCount[index]):
                clock.extend([index]*numCount[index])

    if b == 0:
        clock1 = clock
    else:
        clock2 = clock
        

angles=[[],[]]
for a, wList in zip(range(2), [clock1, clock2]):
    for x in range(1, len( clock1)):
        angles[a].append(wList[x]-wList[x-1])

    angles[a].append((360000-wList[-1])+wList[0])

indexToGoTo = [0] * len(angles[0])

lenPreSuf = 0
indexOn = 1

while indexOn < len(angles[0]):
    if angles[0][indexOn] == angles[0][lenPreSuf]:
        lenPreSuf += 1
        indexToGoTo[indexOn] = lenPreSuf
        indexOn += 1

    elif lenPreSuf != 0:
        lenPreSuf = indexToGoTo[lenPreSuf-1]

    else:
        indexToGoTo[indexOn] = 0
        indexOn += 1


angles[1] *= 2

indexOnSub=0
indexOnStr=0

loops=0
while indexOnStr < len(angles[1]):
    if angles[0][indexOnSub] == angles[1][indexOnStr]:
        indexOnStr += 1
        indexOnSub += 1

        if indexOnSub == len(angles[0]):
            print("possible")
            quit()
            
    elif indexOnSub != 0:
        indexOnSub = indexToGoTo[indexOnSub-1]

    else:
        indexOnStr += 1

    loops+=1
    
print("impossible")
