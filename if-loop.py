n=5
k=(2*n)-2 #8

for i in range(0,n): #(0,1,2,3,4)
    for j in range(0,n-i-1): #(0,1,2,3,4,5,6,7)
        print(end=" ")
    #k-=2 #k=k-2
    for j in range(0,i+1):
        print(" + ",end=" ")
    print("")