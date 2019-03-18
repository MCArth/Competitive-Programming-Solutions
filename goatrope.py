b = [int(a) for a in input().rstrip().split()]
#corners
if b[0] < b[2] and b[1] < b[3]:
    print(pow((b[0]-b[2])**2+(b[1]-b[3])**2, 1/2))

elif b[0] > b[4] and b[1] > b[5]:
    print(pow((b[0]-b[4])**2+(b[1]-b[5])**2, 1/2))

elif b[0] < b[2] and b[1] > b[5]:
    print(pow((b[0]-b[2])**2+(b[1]-b[5])**2, 1/2))

elif b[0] > b[4] and b[1] < b[3]:
    print(pow((b[0]-b[4])**2+(b[1]-b[3])**2, 1/2))

#sides

elif b[1] > b[5]:
    print(b[1]-b[5])

elif b[1] < b[3]:
    print(b[3]-b[1])

elif b[0] > b[4]:
    print(b[0]-b[4])
elif b[0] < b[2]:
    print(b[2]-b[0])

