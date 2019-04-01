import sys

i=0


for x in sys.stdin:
    if i == 0:
        l1=x.split()
    else:
        l2=x.split()

    i+=1

size=l1[0]
changesWant=int(l1[1])
broken=l2
broken = [int(a) for a in broken]

answer=[0]
changes = 0
prevUsed = False

for a in range(1,int(size)):
    if prevUsed == True:
        answer.append(0)
        prevUsed = False

    elif a+1 in broken:
        answer.append(0)
        prevUsed = False

    elif changesWant%2==1:

        if a==1:
            answer.append(0)
            prevUsed = False
        
        if changes < changesWant-1:
            answer.append(1)
            changes+=2
            prevUsed=True
            
        else:
            answer.append(0)
            prevUsed = False

    elif changes < changesWant:
        answer.append(1)
        changes+=2
        prevUsed=True

    else:
        answer.append(0)
        prevUsed = False

if changesWant%2==1:
    if changes < changesWant:
        answer[0]=1

for x in answer:
    sys.stdout.write(str(x))

