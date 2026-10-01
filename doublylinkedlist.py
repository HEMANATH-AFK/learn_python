class Node:
    def __init__(self,data):
        self.data = data 
        self.next = self.prev = None  
class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None 
    def insertAtBegin(self,n):
        newnode = Node(n)
        if self.head is None:
            self.head = self.tail = newnode 
            return 
        newnode.next = self.head 
        self.head.prev = newnode 
        self.head = newnode
    def insertAtEnd(self,n):
        newnode = Node(n)
        if self.head is None:
            self.head = self.tail = newnode 
            return 
        self.tail.next = newnode
        newnode.prev = self.tail 
        self.tail = newnode
    def deleteAtBegin(self):
        if self.head is None:
            print('List is Empty/Delete')
            return 
        if self.head is self.tail:
            self.head = self.tail = None 
            return 
        self.head = self.head.next 
        self.head.prev = None
    def deleteAtEnd(self):
        if self.head is None:
            print('List is Empty/Delete')
            return 
        if self.head is self.tail:
            self.head = self.tail = None 
            return
        self.tail = self.tail.prev 
        self.tail.next = None
    def display(self,c):
        if c == 'F':
            temp = self.head 
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next 
        else:
            temp = self.tail 
            while temp!=None:
                print(temp.data,end=' ')
                temp = temp.prev 

obj = DoublyLinkedList()
obj.insertAtBegin(10)
obj.insertAtBegin(7)
obj.insertAtEnd(15)
obj.insertAtEnd(23)
obj.deleteAtBegin()
obj.deleteAtEnd()
obj.display('F')