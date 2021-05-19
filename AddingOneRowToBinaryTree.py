'''
In this question we have to add one row to binary tree at cetrain depth, we maintain an variable called
direction to get to know where it's a left subtree or right subtree
'''

def addOne(self,root,value,depth):
    def dfs(node,h,dr):
        if h == depth:
            temp = TreeNode(value)
            if dr == 0:
                temp.left = node
            else:
                temp.right = node

            return temp

        if not node: return node

        node.left = dfs(node.left,h+1,0)
        node.right = dfs(node.right,h+1,1)
        return node
    return dfs(root,1,0)