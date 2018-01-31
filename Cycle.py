class Graph:
    def __init__(self,v):
        self.graph=[[]for i in range(v)]
        self.V=v
    def addEdge(self,x,y):
        self.graph[x].append(y)
    def IscycleUnitil(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True
        for ne in self.graph[v]:
            if visited[ne]==False:
                if self.IscycleUnitil(ne,visited,recstack)==True:
                    return True
            elif recstack[ne]==True:
                return True
    def iscycle(self):
        visited=[False]*self.V
        recstack=[False]*self.V
        for node in range(self.V):
            if visited[node]==False:
                if self.IscycleUnitil(node,visited,recstack)==True:
                    return True
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1,2)
g.addEdge(2,3)

if g.iscycle():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")