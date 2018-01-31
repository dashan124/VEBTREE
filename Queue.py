class Qnode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,x):
        newnode = Qnode(x)
        if self.isEmpty() is True:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode
    def isEmpty(self):
        t=self.front
        if t is None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty() is True:
            return None
        else:
            x=self.front.data
            self.front=self.front.next
            return x
q=Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(5)
print(q.isEmpty())
print(q.dequeue())

