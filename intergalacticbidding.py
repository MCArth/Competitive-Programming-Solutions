import sys
from operator import itemgetter
i=0
prices=[]
for x in sys.stdin:
    x=x.rstrip().split()
    if i==0:
        toMake=int(x[1])
        i+=1
    else:
        prices.append((int(x[1]), x[0]))


prices.sort(key=itemgetter(0), reverse=True)
winners=[]
total=0
for x in prices:
    if total+x[0] <= toMake:
        total+=x[0]
        winners.append(x[1])

if total==toMake:
    print(len(winners))
    print(*winners, sep='\n')
else:
    print('0')
