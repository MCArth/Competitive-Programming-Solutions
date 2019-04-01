word = list(input().rstrip())

for i in range(len(word)):
    if ord(word[i]) > 96 and ord(word[i]) < 122:
        word[i] = chr(ord(word[i])+1)
    elif ord(word[i]) == 122:
        word[i] = 'A'

print(*word, sep='')
