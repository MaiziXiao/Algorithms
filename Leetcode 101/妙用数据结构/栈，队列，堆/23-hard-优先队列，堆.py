from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        给你一个链表数组，每个链表都已经按升序排列。

        请你将所有链表合并到一个升序链表中，返回合并后的链表。

        示例 1：
        输入：lists = [[1,4,5],[1,3,4],[2,6]]
        输出：[1,1,2,3,4,4,5,6]
        解释：链表数组如下：
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        将它们合并到一个有序链表中得到。
        1->1->2->3->4->4->5->6
        """
        # Solution1遍历列表，存储值然后sort
        self.nodes = []
        head = point = ListNode(0)
        for a in lists:
            while a:
                self.nodes.append(a.val)
                a = a.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

        # 首先把 k 个链表的首元素都加入最小堆中，它们会自动排好序。
        # 然后我们每次取出最小的那个元素加入我们最终结果的链表中，然后把取出元素的下一个元素再加入堆中，
        # 下次仍从堆中取出最小的元素做相同的操作，以此类推，直到堆中没有元素了，此时 k 个链表也合并为了一个链表，返回首节点即可。
        # 时间复杂度O(logk N)  k是链表数量，n一共的node
