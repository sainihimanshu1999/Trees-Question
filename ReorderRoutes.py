'''
In this question we are doing dfs in graph and if the direction of dfs and roads are smae we are incrementing
the result
'''
import collections

def reorderRoutes(self,connections):
    graph = collections.defaultdict(list)
    roads = set()

    for u,v in connections:
        graph[u].append(v)
        graph[v].append(u)
        roads.add((u,v))

    self.result = 0

    def dfs(u,parent):
        self.result += (parent,u) in roads
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v,u)

    dfs(0,-1)
    return self.result
    
