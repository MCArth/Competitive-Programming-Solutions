import sys

i=0
for x in sys.stdin:
    if i == 0:
        bottles = x

    else:
        sizes = x.split()
    i+=1

sizes = [int(a) for a in sizes]

sizes.sort()
lowestFrac = 1

for x in range(int(bottles)):
    if sizes[x]>x+1:
        print("impossible")
        quit()

    else:
        frac = sizes[x]/(x+1)
        if frac < lowestFrac:
            lowestFrac = frac

print(lowestFrac)
