'''
A valid Bst is when left<parent<right
'''

def isValidBst(self,root):
    def helper(node,left,right):
        if not node:
            return True
        
        if not left<node.val<right:
            return False

        return helper(node.left,left,node.val) and helper(node.right,right,node.val)

    return helper(root,float('-inf'),float('inf'))