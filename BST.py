class BstNode:
    def __init__(self):
        self.data=None
        self.parent=None
        self.right=None
        self.left=None
        self.height=1
class BST:
    def __init__(self):
        self.root=None
    def minimum(self,p):
        while p.left!=None:
            p=p.left
        return p.data
    def Height(self,x):
        if x.left==None and x.right==None:
            return 1
        elif x.left==None and x.right!=None:
            return x.right.height+1
        elif x.right==None and x.left!=None:
            return x.left.height+1
        else:
            r=x.right.height
            h=x.left.height
            if r>h:
                return r+1
            else:
                return h+1
    def H(self,p):
        if p is not None:
            while p!=None:
                p.height=self.Height(p)
                p=p.parent
    def maximum(self,p):
        while p.right!=None:
            p=p.right
        return p.data
    def FindHeight(self,root):
        if root is None:
            return -1
        lh=self.FindHeight(root.left)
        rh=self.FindHeight(root.right)
        if lh>rh:
            return lh+1
        else:
            return rh+1
    def search(self,p,val):
        if self.root is None:
            print("tree is Empty")
            return
        if val==p.data:
            return p
        if val>p.data:
            self.search(p.right,val)
        else:
            self.search(p.left,val)
    def successor(self,x,val):
        if x.right!=None:
            return self.minimum(x.right)
        y=x.parent
        while x!=y.left and y!=None:
            x=y
            y=y.parent
        return y
    def predesssor(self,x,val):
        if x.left!=None:
            return self.maximum(x.left)
        y=x.parent
        while x!=y.right and y!=None:
            x=y
            y=y.parent
        return y
    def mindiff(self,p):
        if p is None:
            return None
        if p.left is not None:
            pass
    def insert(self,p,x):
        b=BstNode()
        b.right=b.left=b.parent=None
        b.data=x
        if self.root is None:
            self.root=b
            #self.Height(self.root)
        if p is not None:
            if x>p.data:
                if p.right is None:
                    p.right=b
                    b.parent=p
                    self.H(b)
                else:
                    self.insert(p.right,x)
            else:
                if p.left is None:
                    p.left=b
                    b.parent=p
                    self.H(b)
                else:
                    self.insert(p.left,x)
    def delete(self,val):
        if self.root is None:
            print("Empty tree ")
            return
        p=self.search(self.root,val)
        if p==self.root:
            if p.left is not None:
                y=self.predesssor(self.root,val)
                p.data=y.data
                self.delete()
                pass
    def leveloreder(self,p):
        if p is not None:
            queue=[]
            queue.append(p)
            while len(queue)!=0:
                x=queue.pop(0)
                print(x.data,x.height)
                if x.left is not None:
                    queue.append(x.left)
                if x.right!=None:
                    queue.append(x.right)
    def inorder(self,p):
        if p is not None:
            self.inorder(p.left)
            print(p.data,p.height)
            self.inorder(p.right)
    def InorderIter(self,p):
        stack=[]
        root=self.root
        x=True
        while x:
            if root!=None:
                stack.append(root)
                root=root.left
            else:
                if len(stack)!=0:
                    root=stack.pop()
                    print(root.data)
                    root=root.right
    def preorder(self,p):
        stack=[]
        root=self.root
        while root!=None or len(stack)!=0:
            if root!=None:
                stack.append(root)
                root=root.left
            else:
                if len(stack)!=0:
                    x=stack[-1]
                else:
                    x=None
                if x==None:
                    print(x.data)
                    while len(stack)!=0 and x:
                        pass
                        
b=BST()
b.insert(b.root,7)
b.insert(b.root,5)
b.insert(b.root,10)
b.insert(b.root,11)
b.insert(b.root,8)
b.insert(b.root,2)
b.insert(b.root,6)
#print(b.search(b.root,2).data)
b.inorder(b.root)