'''
we have to find redundant connections in the graph and make it a tree. A simple connected graph with no
cycle is a tree, hence we have to find a cycle in it. A way to find a cycle is union and find method.
'''

def redundantConnections(self,edges):
    parent = [0]*len(edges)

    def find(x):
        if parent[x] == 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        rootx = find(x)
        rooty = find(y)
        if rootx == rooty:
            return False
        parent[rootx] =rooty

    for x,y in edges:
        if not union(x-1,y-1):
            return [x,y]