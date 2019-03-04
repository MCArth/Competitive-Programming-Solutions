import sys

# Solution to: https://open.kattis.com/problems/erase

p=0
for x in sys.stdin:
    if p == 0:
        overTimes = int(x.rstrip())

    elif p == 1:
        line1 = [int(a) for a in list(x.rstrip())]
    else:
        line2 = [int(a) for a in list(x.rstrip())]

    p += 1

overTimes = overTimes % 2

if overTimes == 0:
    if line1 == line2:
        output = "Deletion succeeded"
    else:
        output = "Deletion failed"


else:
    for i in range(len(line2)):
        if line2[i] == 0:
            line2[i] = 1
        else:
            line2[i] = 0

    if line1 == line2:
        output = "Deletion succeeded"
    else:
        output = "Deletion failed"


print(output)
