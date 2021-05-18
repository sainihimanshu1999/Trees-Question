def evenOdd(self,root):
    q = [root]
    is_even = True
    while q:
        prev = None
        for i in range(len(q)):
            node = q.pop(0)

            if is_even:
                if node.val%2==0: return False
                if prev and prev.val>=node.val: return False

            else:
                if node.val%2==1: return False
                if prev and prev.val<=node.val:return False

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        prev = node
        is_even = not is_even
    return True