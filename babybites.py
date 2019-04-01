import sys
i=0
for x in sys.stdin:
    if i==0:
        pass
    else:
        x=x.rstrip().split()
        
        for a in range(len(x)):
            if x[a]=="mumble":
                pass
            elif int(x[a]) != a+1:
                print("something is fishy")
                quit()
    i+=1

print("makes sense")
