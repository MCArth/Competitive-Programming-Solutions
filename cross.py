import sys
for x in sys.stdin:
    x=x.rstrip().split()
    word1=x[0]
    word2=x[1]
    
word2=list(word2)
word1=list(word1)
for x in word1:
    if x in word2:
        sharedLetter=x
        break

indexword1 = word1.index(sharedLetter)
indexword2 = word2.index(sharedLetter)

for y in range(len(word2)):
    if y==indexword2:
        print(*word1, sep='')
    else:
        for x in range(len(word1)):
            if x==indexword1:
                sys.stdout.write(word2[y])
            else:
                sys.stdout.write('.')

        print()

        
