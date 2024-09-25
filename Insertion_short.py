list1 = []
length = int(input("Enter how many elements in list: "))

for i in range(0,length):
    temp = int(input(f"Enter The {i} Element: "))
    list1.append(temp)
print("Entered List is: ", list1)

for i in range(1, length):
    temp1 = list1[i]
    list1[i] = None
    for j in range(i, 0,-1):
        if temp1 < list1[j-1]:
            list1[j] = list1[j-1]
            if j-1 == 0:
               list1[j-1] = temp1
            else:
                list1[j-1] = None
        else:
            list1[j] = temp1
            break

print("The sorted list: ",list1)