import sys
i=0
for x in sys.stdin:
    if i==0:
        pass
    elif i==1:
        row1 = [int(a) for a in x.rstrip().split()]
    elif i==2:
        row2 =[int(a) for a in x.rstrip().split()]

    i+=1
high=0
lookinForHigh=True
lookinFor=0
for row in [row1,row2]:
    
    for weight in row:
        if weight > lookinFor and not lookinForHigh:
            high=lookinFor
            lookinFor=weight
        elif lookinForHigh: #Looking for new pair to start
            if weight>high:
                lookinFor=weight
                lookinForHigh=False
        elif weight == lookinFor: #Found pair
            lookinForHigh=True
        elif weight > high:
            high = weight

    if not lookinForHigh:
        high=lookinFor
    lookinFor=0
    lookinForHigh=True
    
print(high)
