'''
In this question we have to finc path sum which include root and leaf
'''

def pathSum2(self,root,targetSum):
    if not root: return None

    self.result = []

    def dfs(node,target,path):
        if not node: return 

        if not node.right and not node.left and node.val == target:
            path.append(node.val)
            self.result.append(path)

        dfs(node.left,target-node.val,path+[node.val])
        dfs(node.right,target-node.val,path+[node.val])

    dfs(root,targetSum)
    return self.result
