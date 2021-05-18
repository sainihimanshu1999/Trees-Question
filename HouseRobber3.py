'''
we make two variable now and later, now will have same node.val and other node.val total and later will
have next node and other node
'''

def houseRobber(self,root):
    def dfs(node):
        if not node: return (0,0)

        left,right = dfs(node.left),dfs(node.right)

        now = node.val + left[1] + right[1]
        later = max(left)+max(right)

        return max((now,later))

    return max(dfs(root))