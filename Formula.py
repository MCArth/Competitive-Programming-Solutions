from sys import stdin
p = 0
coords = []
for x in stdin:
    if p < 3:
        coords.append([int(a) for a in x.rstrip().split()])

    else:
        r = float(x.rstrip())

    p += 1

le = []

for i in range(-1, 2):
    le.append(pow((coords[i][0]-coords[i+1][0])**2+(coords[i][1]-coords[i+1][1])**2, 1/2))

A = (1/4)*pow(4 *le[0]**2 * le[1]**2 - (le[0]**2 + le[1]**2 - le[2]**2)**2, 1/2)

newR = (2*A)/(le[0]+le[1]+le[2])

print(((newR/r)-1)*100)
