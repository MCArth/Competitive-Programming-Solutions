import sys

# Solution to: https://open.kattis.com/problems/judging

p=0
kattis = {}

DOM = {}
for x in sys.stdin:
    if p==0:
        probsTotal = int(x.rstrip())

    elif p > probsTotal:
        kattis[x.rstrip()] = kattis.get(x.rstrip(), 0)+1


    else:
        DOM[x.rstrip()] = DOM.get(x.rstrip(), 0)+1

    p += 1


total = 0
for i in kattis:
    total += min(kattis[i], DOM.get(i, 0))

print(total)
