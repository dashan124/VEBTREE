class StackNode:
    def __init__(self):
        self.data=None
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,x):
        new_node=StackNode()
        new_node.data=x
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.head is None:
            print("stack is empty ")
            return
        t=self.head.data
        self.head=self.head.next
        return t
    def top(self):
        if self.head is None:
            print("Empty stack")
            return
        t=self.head.data
        return t
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def printstack(self):
        temp=self.head
        if temp is None:
            return
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def sortedinsert(self,val):
        new_node = StackNode()
        new_node.data = val
        if self.head is None:
            self.head = new_node
            return
        if val < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next != None and temp.data < val:
            temp = temp.next
        temp.next = new_node
s=Stack()
s.sortedinsert(6)
s.sortedinsert(9)
s.sortedinsert(4)
s.sortedinsert(12)
s.printstack()