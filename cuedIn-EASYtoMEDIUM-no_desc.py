from sys import stdin
first = True
colours = {'red': 0, 'yellow': 1, 'green': 2, 'brown': 3, 'blue': 4, 'pink': 5, 'black': 6}
count = [0] * 7
secCount = [0] * 7
red = 0
other = 0
for x in stdin:
    if first:
        first = False

    else:
        count[colours[x.rstrip()]] += 1
        
        if x.rstrip() != 'red':
            secCount[colours[x.rstrip()]] += 1

maxPoint = 0
pointer = 6
prevPotRed = False
potRed = False

while True:
    
    if potRed or pointer == 0:

        if count[0] == 0 and max(secCount) != 0:
            potRed = False
            pointer -= 1
            
        elif count[0] != 0 and not prevPotRed:
            maxPoint += 1
            count[0] -= 1
            potRed = False
            prevPotRed = True
        else:
            break
    
    elif count[pointer] != 0:
        maxPoint += pointer + 1
        potRed = True
        prevPotRed = False

        if count[0] == 0:
            count[pointer] -= 1
            secCount[pointer] -= 1

    else:
        prevPointer = pointer
        pointer -= 1
        
print(maxPoint)
