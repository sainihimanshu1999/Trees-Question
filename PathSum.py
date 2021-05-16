'''
In this question target sum is subtracted in every iteration from node value
'''

def pathSum(self,root,targetSum):
    if not root: return False

    if not root.left  and not root.right and root.val == targetSum:
        return True
    targetSum -= root.val
    return self.pathSum(root.left,targetSum) or self.pathSum(root.right,targetSum)