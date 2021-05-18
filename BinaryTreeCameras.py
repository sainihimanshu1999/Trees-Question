'''
In this question we have to calculate the minimium number of cameras required, in this 0 means not covered
1 mean covered but no camera and 2 mean has camera on it. camera covers itself,parents,immediate children
'''

def Camera(self,root):
    self.cams = 0
    def dfs(node):
        if not node: return 1

        l = dfs(node.left)
        r = dfs(node.right)

        if l == 0 or r ==0:
            self.cams += 1
            return 2

        if l ==2 or r ==2:
            return 1
        else:
            return 0

    if dfs(root) == 0:
        self.cams +=1
    return self.cams