'''
In this question we have to find the second minimum node in special tree
'''

def secondMin(self,root):
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1<node.val<self.ans:
                self.ans = node.val
            elif min1 == node.val:
                dfs(node.left)
                dfs(node.right)


    return self.ans if self.ans<float('inf') else -1