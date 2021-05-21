'''
Whenever we have to convert sorted array to bst alwasy bear in mind, that sorted array can easily go
through inorder.Hence we use inorder insertion
'''

def sortedArrayToBST(self,nums):

    if  not nums: return None

    mid = len(nums)//2

    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
