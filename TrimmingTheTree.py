'''
1. if node.val<low we have to return node.right
2. if node.val>high we have to return node.left
3. if it's in between we check the whole tree

In bst it is not possible to cut the trees from in between
'''

def trim(self,root,low,high):
    def dfs(node):
        if not node: return None

        if node.val<low:
            return dfs(node.right)

        if node.right>high:
            return dfs(node.right)

        else:
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

    return dfs(root)