'''
Graph is the best way to find distance between two nodes
'''
import collections

def distance(self,root,target,k):
    graph = collections.defaultadict(list)
    result = []
    visited = set()

    def dfs(node):
        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            dfs(node.left)

        if node.right:
            graph[node].append(node.left)
            graph[node.right].append(node)
            dfs(node.right)

    dfs(root)

    def dfs2(node,dist):
        if dist<k:
            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    dfs2(node,d+1)
        else:
            result.append(node.val)

    dfs2(target,0)
    return result