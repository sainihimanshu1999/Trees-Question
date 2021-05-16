'''
In this question we have to check that whether or not linked list path can be found in BST
'''

def isSubPath(self,head,root):
    def helper(head,node):
        if not head: return True
        if not node: return False

        if head.val == node.val:
            return helper(head.next,node.left) or helper(head.next, node.right)

        return False

    if not head: return True
    if not root: return False
    if helper(head,root): return True

    return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)