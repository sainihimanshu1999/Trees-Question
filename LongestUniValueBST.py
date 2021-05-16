'''
In this question when parent node val is equal to child node value then we increment it by one
'''

def longestUniVal(self,root):
    self.count = 0

    def helper(node):
        if not node:
            return 0

        left = helper(node.left)
        right = helper(node.right)

        left = left+1 if node.left and node.left.val == node.val else 0
        right = right+1 if node.right and node.right.val ==node.val else 0

        self.count = max(self.count,left+right)

        return max(left,right)

    helper(root)
    return self.count