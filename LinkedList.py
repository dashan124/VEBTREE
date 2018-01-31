class Listnode:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,x):
        new_node=Listnode()
        new_node.data=x
        new_node.next=self.head
        self.head=new_node
    def Insert(self,p,x):
        if p is None:
            print("the given previous node should be in the linked list")
            return
        new_node=Listnode()
        new_node.data=x
        new_node.next=p.next
        p.next=new_node
    def append(self,x):
        new_node=Listnode()
        new_node.data=x
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next!=None:
            last=last.next
        last.next=new_node
    def printlist(self):
        if self.head is None:
            return None
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
l=LinkedList()
l.insert(1)
l.insert(4)
l.Insert(l.head,6)
l.append(9)
l.printlist()