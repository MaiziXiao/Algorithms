
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 中序遍历
        def helper(head):
            if head:
                helper(head.left)
                print(head.val)
                helper(head.right)
