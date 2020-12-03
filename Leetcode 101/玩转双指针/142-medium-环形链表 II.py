# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
        如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
        说明：不允许修改给定的链表。

        进阶：

        你是否可以使用 O(1) 空间解决此题？
        """
        slow, fast = head, head
        # 第一步，快慢指针，快指针走两步，慢指针走一步。如果相等有环，如果快指针走到None,没环。需要考虑只有一个节点的特殊情况
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        # 第二步，具体的方法为，首先假定链表起点到入环的第一个节点A的长度为a【未知】，
        # 到快慢指针相遇的节点B的长度为（a + b）【这个长度是已知的】。现在我们想知道a的值，
        # 注意到快指针p2始终是慢指针p走过长度的2倍，所以慢指针p从B继续走（a + b）又能回到B点，
        # 如果只走a个长度就能回到节点A。但是a的值是不知道的，解决思路是曲线救国，注意到起点到A的长度是a，
        # 那么可以用一个从起点开始的新指针q和从节点B开始的慢指针p同步走，相遇的地方必然是入环的第一个节点A。
        fast = head
        while fast != head:
            fast = fast.next
            slow = slow.next
        return slow
