import sys
i=0
lowestPrice=1000000
applicable=[]
for x in sys.stdin:
    if i==0:
        lawnSize=int(x.rstrip().split()[0])
        i+=1
    else:
        x=x.rstrip().split(",")

        p=int(x[1])
        c=int(x[2])
        t=int(x[3])
        r=int(x[4])
        
        tCycle = t+r
        cutCycle = c*t

        timeWholeLawn=tCycle*(lawnSize/cutCycle)

        if timeWholeLawn < 10080:
            if p < lowestPrice:
                lowestPrice = p
                applicable=[x[0]]
            elif p == lowestPrice:
                applicable.append(x[0])

if applicable:
    for x in applicable:
        print(x)
else:
    print("no such mower")
