from operator import itemgetter

useless = raw_input().rstrip().split()
x = raw_input().rstrip().split()
deps = [(int(a), i) for a, i in zip(x, range(len(x)))]
deps.sort(reverse = True, key = itemgetter(0))

# index 0 (a) is capacity, b is cost
#buildings = [(int(a), int(b), c+1) for a, b, c in zip(input().rstrip().split(), input().rstrip().split(), range(len(useless[1])))]

list1 = raw_input().rstrip().split()
list2 = raw_input().rstrip().split()
#buildings = [(int(a), int(b), c+1) for a, b, c in zip(list1, list2, range(len(useless[1])))]
buildings = []
for i in range(len(list1)):
    buildings.append((int(list1[i]), int(list2[i]), i))

buildings.sort(key = itemgetter(1))
used = [False] * len(buildings)

buys = []

for z in deps:
    found = False
    for i in range(len(buildings)):
        if not used[i]:
            if buildings[i][0] >= z[0]:
                buys.append((buildings[i][2], z[1]))
                used[i] = True
                found = True
                break

    if not found:
        print("impossible")
        quit()

buys.sort(key = itemgetter(1))
for i in range(len(buys)):
    print(buys[i][0]+1),
