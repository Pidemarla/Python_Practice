list1 = [8,4,9,2,7,44,22,8,99]
length = len(list1)
for i in range(0,length):
    for j in range(0,length-1-i):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
print(list1)
        