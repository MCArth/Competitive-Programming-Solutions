from sys import stdin
from operator import itemgetter
first = True
myList = []

for x in stdin:
    if first:
        first = False
    else:
        myList.append([int(a) for a in x.rstrip().split()])

invest = 1
lastHour = 0
g = 49
notSecond = False

myList.sort(key = itemgetter(0))
for x in myList:
    if x[1] < g:
        if notSecond:
            invest *= pow(2, (x[0] - lastHour)/g)
        else:
            notSecond = True

        g = x[1]
        lastHour = x[0]

                
invest *= pow(2, (24 - lastHour)/g)
print(invest)

