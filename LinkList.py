
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next

    def insert_at_end(self,data):
        if self.head is None:
            self.head = node(data)
            return
        new_node = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_before(self,data,new_data):
        if self.head is None:
            self.head = node(new_data)
            return
        if self.head.data == data:
            self.insert_at_begin(new_data)
            return
        new_node = node(new_data)
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def insert_after(self,data,new_data):
        if self.head is None:
            self.head = node(new_data)
            return
        new_node = node(new_data)
        temp = self.head
        while temp.data != data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at(self,data):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return
        while temp.next.data != data:
            temp = temp.next
        temp.next = temp.next.next

li= LinkList()

li.insert_at_end(4)
li.insert_at_end(3)
li.insert_at_end(2)
# li.insert_before(2,7)
li.delete_at(2)
li.print_list()
