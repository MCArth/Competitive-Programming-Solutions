from sys import stdin
p = 0
sizes = []
for x in stdin:
    x = int(x.rstrip())
    if p == 0:
        width = x*10000000
    elif p == 1:
        p += 1
        continue
    else:
        sizes.append(x)
    p += 1

needed = {}
solutions = []

for i in range(len(sizes)):
    x = sizes[i]
    if width-x in needed:
        solutions.append(((width-x, needed[width-x]), (x, i+1)))

    needed[x] = needed.get(x, i+1)

currMax = -1

for x in solutions:
    if abs(x[0][0]-x[1][0]) > currMax:
        currMax = abs(x[0][0]-x[1][0])
        a1 = x[0][0]
        a2 = x[1][0]

if not solutions:
    print("danger")
    
else:
    print("yes " + str(min(a1, a2)) + " " + str(max(a1, a2)))
