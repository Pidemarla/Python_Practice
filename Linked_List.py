class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
         
    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"Inserted data at begining {data}")
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"Inserted {data} at the end")

    def insert_at_begin(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        self.head = new_node
        new_node.next = temp
        print(f"Inserted {data} at the Beggining")

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print(None)
    def length(self):
        count = 0
        if self.head is None:
            return count
        
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next
        return count
    def insert_at_position(self,pos,data):
        len = self.length()
        new_node = Node(data)
        count = 1
        temp = self.head
        if pos <= 0 or pos > len+1:
            print(f"Out of Scope, Enter a Valid Position between 1 and {len+1}")
            return
        while count< pos-1:
            temp = temp.next
            count = count+1
        temp2 = temp.next
        temp.next = new_node
        new_node.next = temp2
        print(f"Inserted {data} at the position {pos}")
    
    def delete_from_beginning(self):
        temp = self.head
        self.head = temp.next
        tempdata = temp.data
        temp.data = None
        temp.next = None
        print(f"The data at beginning {tempdata} and the link is deleted")
    
    def delete_from_end(self):
        temp = self.head
        lastbutone = None

        while temp.next:
            lastbutone = temp
            temp = temp.next

        tempdata = temp.data
        temp.data = None
        lastbutone.next = None

        print(f"Deleted {tempdata} from the end")
        
    def delete_from_position(self,pos):
        len = self.length()
        count = 1
        temp = self.head
        if pos <= 0 or pos > len+1:
            print(f"Out of Scope, Enter a Valid Position between 1 and {len+1}")
            return
        while count< pos-1:
            temp = temp.next
            count = count+1
        temp2 = temp.next
        temp3 = temp2.next
        temp.next = temp3
        print(f"deleted data at the position {pos}")

    def Binary_search(self,value):
        len = self.length()
        if self.length() == 0:
            print("There is no Elements in the List")
            return
        
        temp = self.head
        count = 1
        while temp:
            if temp.data == value:
                return count
            else:
                temp = temp.next
                count = count + 1
        if count == len+1:
            print("Element is not in the List")
            return None
        print(f"The position of the Value is {count}")


lk_lst = Linked_List()
lk_lst.append(1)
lk_lst.append(2)
lk_lst.append(3)
lk_lst.append(4)
lk_lst.insert_at_begin(0)
# print(lk_lst.length())
lk_lst.insert_at_position(2,9)
lk_lst.display()
# position = lk_lst.Binary_search(5)

lk_lst.delete_from_beginning()
lk_lst.display()
lk_lst.delete_from_end()
lk_lst.display()
lk_lst.delete_from_position(2)
lk_lst.display()