inp1 = input()
inp2 = input()

if len(inp1) != len(inp2):
    print("impossible")
    quit()

linp1 = [0]*300
linp2 = [0]*300

for x in inp1:
    linp1[ord(x)] += 1


for x in inp2:
    linp2[ord(x)] += 1

if linp1 == linp2:
    print("possible")

else:
    print("impossible")
