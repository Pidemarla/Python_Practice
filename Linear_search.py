list1 = []
length = int(input("Enter how many elements in list: "))
for i in range(0,length):
    temp = int(input(f"Enter The {i} Element: "))
    list1.append(temp)
print("Entered List is: ", list1)
Target = int(input("Enter the number to be searched: "))
position = None
for i in range(0,length):
    if list1[i] == Target:
        position = i
        break
if position == None:
    print("Element is not in the list")
else:
    print("The position  of the target Element is: ", position)