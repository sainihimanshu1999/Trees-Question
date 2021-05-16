'''
In this question we have to calculate individual sum of subtrees and then subtract from total sum of
subtree
'''

def maxiProd(self,root):
    a = []
    def subtree(node):
        if not node:
            return 0
        ans = node.val + subtree(node.left) + subtree(node.right)
        a.append(ans)
        return ans

    total = subtree(root)
    return max((x*(total-x)) for x in a)
