import sys
i=0
for x in sys.stdin:
    x=[int(a) for a in x.rstrip().split()]
    if i==0:
        pass
    elif i==1:
        clock1 = x
        clock1.sort()

    elif i==2:
        clock2 = x
        clock2.sort()
    i+=1
    
angles=[[],[]]
for a, wList in zip(range(2), [clock1, clock2]):
    for x in range(1, len( clock1)):
        angles[a].append(wList[x]-wList[x-1])

    angles[a].append((360000-wList[-1])+wList[0])


if ' '.join(map(str, angles[0])) in ' '.join(map(str, angles[1] * 2)):
    print("possible")
else:
    print("impossible")
