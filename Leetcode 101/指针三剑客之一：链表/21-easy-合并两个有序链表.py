# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

        示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        new_head = ListNode()
        point = new_head
        while l1 or l2:
            if l1 and (not l2):
                new_head.next = l1
                return point.next
            elif l2 and (not l1):
                new_head.next = l2
                return point.next
            else:
                if l1.val <= l2.val:
                    # In place
                    new_head.next = l1
                    l1 = l1.next
                else:
                    new_head.next = l2
                    l2 = l2.next
            new_head = new_head.next
        return point.next
