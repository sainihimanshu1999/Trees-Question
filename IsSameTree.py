'''
this question need you to prove is tree are same or not
'''

def isSameTree(self,p,q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    else:
        return p==q


