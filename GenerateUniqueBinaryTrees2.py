'''
This question was pretty tough, we have to make every node a root once and calculate it's bst
'''

def uniqueBST2(self,n):
    if n ==0:
        return None

    def dfs(start,end):
        if start == end:
            return None
        result = []
        for i in range(start,end):
            for l in dfs(start,i):
                for r in dfs(i+1,end):
                    node = TreeNode(i)
                    node.left,node.right = l,r
                    result.append(node)
        return result