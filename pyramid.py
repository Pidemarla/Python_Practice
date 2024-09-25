n = int(input("Enter the Number: "))
for i in range(1,n+1):
    k=1
    for j in range(n+1-i,0,-1):
        print(" ",end="")
    for m in range(2*i-1):
        if k%2!=0:
            print("*",end="")
        else:
            print(" ",end="")
        k+=1
    print("")
