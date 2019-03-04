# Solution to: https://open.kattis.com/problems/nimionese

theStrUpper = input()
theStr = list(theStrUpper.lower())

hards = ['b','c','d','g','k','n','p','t']
ords = [ord(x) for x in hards]

soft = ['a','o','u']
softOrds = [ord(x) for x in soft]

newWord = True
subSyll = False
indexAdd = []
for i in range(len(theStr)):
    if newWord and theStr[i] not in hards:
        minDist = 100
        minOrd = 0
        for num in ords:
            if abs(ord(theStr[i]) - num) < minDist:
                minDist = abs(ord(theStr[i]) - num)
                minOrd = num

            elif abs(ord(theStr[i]) - num) == minDist and num < minOrd:
                minOrd = num
                minDist = abs(ord(theStr[i]) - num)

        theStr[i] = chr(minOrd)

    if newWord:
        startHard = theStr[i]
    elif theStr[i] == '-':
        subSyll = True
        
    if subSyll and theStr[i] in hards:
            theStr[i] = startHard

    if theStr[i] == ' ':
        newWord = True
        subSyll = False
    else:
        newWord = False
        
    if i < len(theStr)-1:
        if theStr[i+1] == ' ' and theStr[i] in hards:
            minDist = 100
            minOrd = 0
            for num in softOrds:
                if abs(ord(theStr[i]) - num) < minDist:
                    minDist = abs(ord(theStr[i]) - num)
                    minOrd = num

                elif abs(ord(theStr[i]) - num) == minDist and num < minOrd:
                    minOrd = num
                    minDist = abs(ord(theStr[i]) - num)

            indexAdd.append([i, chr(minOrd) + 'h'])

    elif i == len(theStr)-1 and theStr[i] in hards:
        minDist = 100
        minOrd = 0
        for num in softOrds:
            if abs(ord(theStr[i]) - num) < minDist:
                minDist = abs(ord(theStr[i]) - num)
                minOrd = num

            elif abs(ord(theStr[i]) - num) == minDist and num < minOrd:
                minOrd = num
                minDist = abs(ord(theStr[i]) - num)

        indexAdd.append([i, chr(minOrd) + 'h'])

    if theStrUpper[i].isupper():
        theStr[i] = theStr[i].upper()


counter = 0
for i in range(len(theStr)):
    if theStr[i] != '-':
        print(theStr[i], end = '')
        
    if counter < len(indexAdd):
        if indexAdd[counter][0] == i:
            print(indexAdd[counter][1], end = '')
            counter += 1
