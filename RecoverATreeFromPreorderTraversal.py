'''
In this question we maintain a stack and work accordingly
'''

def recoveringTree(self,nums):
    stack,i = [],0
    while i<len(nums):
        level,val =0,''
        while i<len(nums) and nums[i] == '-':
            level +=1
            i +=1
        while i<len(nums) and nums[i]!='-':
            val += nums[i]
            i +=1

        while len(stack)>level:
            stack.pop()
        node = TreeNode(val)
        
        if stack and stack[-1].left is None:
            stack[-1].left  = node
        elif stack:
            stack[-1].right = node

        stack.append(node)
    return stack[0]