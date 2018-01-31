class RBNode:
    def __init__(self):
        self.data=None
        self.color="black"
        self.parent=None
        self.right=None
        self.left=None
class RB:
    def __init__(self):
        self.root=None
    def LeftRotate(self):
        pass
    def RightR(self):
        pass
    def Fix(self,z):
        while z.parent.color=="red":
            if z.parent==z.parent.parent.left:
                y=z.parent.parent.left
                if
    def Insert(self,val):
        z=RBNode()
        z.data=val
        y=None
        x=self.root
        while x!=None:
            y=x
            if z.data<x.data:
                x=x.left
            else:
                x=x.right
        z.parent=y
        if z.data<y.data:
            y.left=z
        else:
            y.right=z
        z.left=None
        z.right=None
        z.color="red"
        self.Fix(z)