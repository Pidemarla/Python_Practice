list1 = []
length = int(input("Enter how many elements in list: "))
for i in range(0,length):
    temp = int(input(f"Enter The {i} Element: "))
    list1.append(temp)
print("Entered List is: ", list1)
for i in range(0, length):
    for j in range(0,length-1-i):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
print("The sorted list: ",list1)