'''
In this question we have to count 3 subtree, l,r and n-(l+r)-1, if the max of them is greater than n/2
then our player wins
'''

def color(self,root,n,x):
    c = [0,0]
    def dfs(node):
        if not node: return 0
        l,r = dfs(node.left),dfs(node.right)
        if node.val == x:
            c[0],c[1] = l,r

        return l+r+1
    return dfs(root)/2 < max(max(c),n-sum(c)-1)