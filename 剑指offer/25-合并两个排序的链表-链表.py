# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

        示例1：

        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        # 1.循环
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        dummy_node = ListNode(None)
        dummy_node.next = head

        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                head.next = l2
                l2 = l2.next
            elif l2 is None:
                head.next = l1
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
            head = head.next
        return dummy_node.next

        # 2.递归
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # pre = None
        # if l1.val < l2.val:
        #     pre = l1
        #     pre.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     pre = l2
        #     pre.next = self.mergeTwoLists(l1, l2.next)
        # return pre
