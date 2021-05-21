'''
In this question we have to find if there exist two nodes whose sum equal to target sum or not
'''

def twoSum(self,root,k):
    if not root: return False
    q,s = [root],set()
    for i in q:
        if k-i.val in s: return True
        s.add(i.val)
        if i.left:q.append(i.left)
        if i.right:q.append(i.right)

    return False