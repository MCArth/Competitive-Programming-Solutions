from operator import itemgetter

word = input().rstrip()
letters = [[word[i], i] for i in range(len(word))]

letters.sort(key = itemgetter(0))
swaps = []
for i in range(len(letters)):

    if letters[i][1] != i:

        for x in range(i+1, len(letters)):
            if letters[x][1] == i:
                swaps.append(([letters[x][0], letters[x][1]],
                              [letters[i][0], letters[i][1]]))
                letters[x][1] = letters[i][1]
                letters[i][1] = i
                
for i in range(len(swaps)-1, -1, -1):
    if swaps[i][0][0] > swaps[i][1][0]:
        print(swaps[i][1][1]+1, swaps[i][0][1]+1)
    else:
        print(swaps[i][0][1]+1, swaps[i][1][1]+1)
