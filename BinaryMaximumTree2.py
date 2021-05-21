'''
In maximum tree the node val is always greater than all other node values, and we have to insert a value 
into it
'''

def maximumBinaryTree(self,root,val):
    if root and root.val>val:
        root.right = self.maximumBinaryTree(root.right,val)
        return root

    node = TreeNode(val)
    node.left = root
    return node