'''
In this question we have to give number of paths in a tree which satisfy the target sum which can not 
include root or leaf node, We have to do this by using two recurrsion
'''

def pathSum(self,root,targetSum):
    self.result = 0

    def dfs(node,target):
        if not node: return None

        numPath(node,target)
        dfs(node.left,target)
        dfs(node.right,target)

    def numPath(node,target):
        if not node: return None

        if node.val == target:
            self.result +=1

        numPath(node.left,target-node.val)
        numPath(node.right,target-node.val)

    dfs(root,targetSum)
    return self.result