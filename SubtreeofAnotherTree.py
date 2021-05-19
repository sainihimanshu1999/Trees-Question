'''
In this question we are given two trees we have to find that if given second tree is the subtree of 
first
'''

def subTree(self,root,subroot):
    if not subroot: return False

    def dfs(node,node2):
        if not node: return False

        if node.val == node2.val  and check(node,node2):
            return True

        return dfs(node.left,node2) or dfs(node.right,node2)

    def check(root1,root2):
        if not root1 and not root2:
            return True
        
        elif root1 and not root2 or root2 and not root1:
            return False

        if root1.val !=root.val:
            return False

        return check(root1.left,root2.left) and check(root1.right,root2.right)

    return dfs(root,subroot)