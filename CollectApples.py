'''
We have to give the mininum time taken to collect the apples
'''
import collections
def collectApples(self,edges,hasApple):
    routes = collections.defaultdict(list)

    for u,v in edges:
        routes[u].append(v)
        routes[v].append(u)

    visited = set()

    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        cost = 0
        for child in routes[node]:
            cost += dfs(child)

        if cost or hasApple[node]:
            return cost + 1
        return 0

    res = dfs(0)
    return 2*(res-1) if res else 0
            


