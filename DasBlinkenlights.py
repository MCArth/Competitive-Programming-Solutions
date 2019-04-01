inp = [int(a) for a in input().rstrip().split()]

smallest = 0

def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a)

a = inp[0]
b = inp[1]

while a != 0:
    a, b = b%a, a

if inp[0]*inp[1]/b <= inp[2]:
    print("yes")
else:
    print("no")
