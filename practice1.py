N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))
list1 = []

for i in range (1,N):
    count1 = 0
    for j in range(1,i):
        if (i % j == 0):
            count1 += 1
    
    if count1 == 1:
        list1.append(i)

