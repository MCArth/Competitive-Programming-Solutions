right = int(input().rstrip())
me = input().rstrip()
fri = input().rstrip()

same = 0
for i in range(len(me)):
    if me[i] == fri[i] and right > 0:
        same += 1
        right -= 1

    elif me[i] != fri[i] and len(me)-i > right:
        same += 1

print(same)
