# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        输入两个链表，找出它们的第一个公共节点。
        """

        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        # 让p1, p2先走自己的链表，走完以后从对方的链表开始走，这样第二次两个节点会同时走到底,
        # 如果直到走到最后一个节点，p1.next 和 p2.next都为 None, 返回None
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return headA

        # 或者两个链表先走一遍算出长度，然后长的链表先走直到和短的一起开始