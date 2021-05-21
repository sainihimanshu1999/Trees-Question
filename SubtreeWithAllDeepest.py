'''
we havr to find the smallet subtree with all the deepest node present in the tree
'''

def subtreeALLDEEP(self,root):
    def dfs(node,depth):
        if not node: return node,depth

        left,lD = dfs(node.left,depth+1)
        right,rD = dfs(node.right,depth+1)

        if lD>rD:
            return left,lD

        if rD>lD:
            return right,rD

        else:
            return node,lD

    return dfs(root,0)[0]