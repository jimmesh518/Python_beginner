'''n = 3 
k = 1
for i in range(n):
    for j in range(i+1):
        print("*", end =" ")
    print("")'''

'''n = 5
for i in range (n): #0,1,2,3,4
    for j in range (n-i):
        print(end=" ")
    for j in range (i+1):
        print("*", end=" ")
    print()

n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    print()'''


for i in range(0,10):
    if i == 5:
        break
    print('Number is ' + str(i))
print('Out of loop')