n = int(input("Enter the num: "))

for i in range(n,0,-1):
    print("* ",end="")
    if i==n:
        for j in range(n-1):
            print("* ",end="")
    else:
        for k in range(2*i):
            if k==2*i-4:
                print("* ",end="")
            else:
                print(" ",end="")
    print()

