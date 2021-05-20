'''
In this question we have to find the most frequent subtree sum
'''

def subtree(self,root):
    if not root: return []

    def dfs(node):
        if not node: return 0

        sumi = node.val + dfs(node.left) + dfs(node.right)

        dic[sumi] = dic.get(sumi,0)+1

        return sumi

    dic = {}
    dfs(root)
    maxCount = max(dic.values())
    return [s for s in dic if dic[s]==maxCount]