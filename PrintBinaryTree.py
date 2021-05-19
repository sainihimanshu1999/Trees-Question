'''
In this question we have to print an binary tree in 2D array of m*n, where rows are equal height
and cols are equal to the width
'''

def printTrees(self,root):
    def height(node):
        if not node: return 0
        return 1+max(node.left,node.right)

    def dfs(node,row,left,right):
        if not node: return None
        mid = (left+right)//2

        self.res[row][mid] = str(node.val)
        dfs(node.left,row+1,left,mid-1)
        dfs(node.right,row+1,mid+1,right)


    h = height(root)
    width = 2**h - 1
    self.result = [[''*width for i in range(height)]]
    dfs(root,0,0,width-1)