import sys
i=0
total=0
output="possible"
for x in sys.stdin:
    x=[int(a) for a in x.rstrip().split()]
    if i==0:
        capacity=x[0]
        stations=x[1]
    else:
        if i==1:
            if x[0]>0:
                output="impossible"

        total+=x[1]-x[0]
        if total > capacity:
            output="impossible"
            
        if total < 0:
            output="impossible"
            
        if x[2]>0:
            if total<capacity:
                output="impossible"

        if i==stations:
            if x[1]>0 or x[2]>0:
                output="impossible"

            if total!=0:
                output="impossible"
    
    i+=1

print(output)
