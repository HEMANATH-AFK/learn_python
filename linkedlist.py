class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 
    def insertAtBegin(self,n):
        newnode = Node(n)
        newnode.next = self.head 
        self.head = newnode
    def insertAtEnd(self,n):
        newnode = Node(n)
        if self.head is None:
            self.head = newnode
            return 
        temp = self.head 
        while temp.next != None:
            temp = temp.next 
        temp.next = newnode
    def insertAtAny(self,pos,n):
        if pos==0:
            self.insertAtBegin(n)
            return 
        newnode = Node(n)
        temp = self.head 
        for i in range(pos-1):
            temp  = temp.next 
            if temp is None:
                print('Out of Range')
                return 
        newnode.next = temp.next 
        temp.next = newnode
    def deleteAtBegin(self):
        if self.head is None:
            print('List is Empty')
            return 
        if self.head.next is None:
            self.head = None 
            return 
        self.head = self.head.next 
    def deleteAtEnd(self):
        if self.head is None:
            print('List is Empty')
            return 
        if self.head.next is None:
            self.head = None 
            return 
        temp = self.head 
        while temp.next.next != None:
            temp = temp.next 
        temp.next = None 
    def deleteAtAny(self,pos):
        if pos==0:
            self.deleteAtBegin()
            return 
        temp = self.head 
        for _ in range(pos-1):
            temp = temp.next 
            if temp.next is None:
                print('Out of Range/Deletion')
                return 
        temp.next = temp.next.next
    def display(self):
        temp = self.head 
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next 

obj = LinkedList()
obj.insertAtBegin(21)
obj.insertAtBegin(17)
obj.insertAtEnd(25)
obj.insertAtEnd(31)
obj.insertAtAny(4,44)
obj.deleteAtAny(5)
obj.display()