'''
In this question we have to point the next pointer to its right node then to null if no right node,
we use BFS in this, we create two node, dummy for parent node and current for level nodes
'''

def rightPointer(self,root):
    node = root
    while node:
        curr = dummy = Node(0)
        while node:
            if node.left:
                curr.next = node.left
                curr = curr.next
            if node.right:
                curr.next = node.right
                curr = curr.next

            node = node.next
        node = dummy.next
    return root