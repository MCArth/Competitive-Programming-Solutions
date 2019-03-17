import sys

i=0

for x in sys.stdin:

    x=x.rstrip()

    if i == 0:

        line = x.split()

        start = int(line[0])-1

    elif i == 1:

        stops = [int(a) for a in x]

        if stops[start] == 1:

            i+=1

        else:
            stops = []

    else:

        newstops = [int(a) for a in x]

        if newstops[start] == 1:

            for b in range(len(stops)):

                if newstops[b] == 1:
                    if stops[b] == 0:
                        stops[b] = 1
        
    if i == 0:
        i+=1

    
    
num=-1


for c in range(len(stops)):
    if stops[c] == 1:
        num+=1
if num == -1:
    print(0)
else:
    print(num)
