waste = input()
times = [int(a) for a in input().rstrip().split()]
dists = [int(a) for a in input().rstrip().split()]

timeDiff = times[1] - times[0]

if len(times) == 2:
    mDists = []
    newDists = []
    for i1 in range(len(dists)-1):
        mDists.append(dists[i1+1]-dists[i1])

    for x in mDists:
        if x not in newDists:
            newDists.append(x)

    print(len(newDists))
    for x in newDists:
        print(int(x), end = " ")

    quit()

speeds = []
for i1 in range(len(dists)-1):
    i2 = i1+1
    
    firstDist = dists[i2] - dists[i1]
    speed = firstDist/timeDiff
    pD = i2+1
    pT = 2
    count = 0

    while pD < len(dists) and not count > 0:
        timeLook = (times[pT]-times[0])*speed + dists[i1]


        if dists[pD] == timeLook:
            count = 0
            if pT+1 == len(times):
                speeds.append(speed)
                break
            
            pT += 1
            pD += 1

        elif dists[pD] > timeLook:
            break

        else:
            pD += 1
            count += 1

speeds.sort()
speedsNew = []
for x in speeds:
    if x not in speedsNew:
        speedsNew.append(x)


print(len(speedsNew))
for x in speedsNew:
    print(int(x*timeDiff), end = " ")

