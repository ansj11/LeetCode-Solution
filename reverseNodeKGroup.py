# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, first, last):
        pre = last
        while first != last:
            t = first.next
            first.next = pre
            pre = first
            first = t
        return pre
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        for i in range(k):
            if not node:
                return head
            node = node.next
        new_head = self.reverseList(head, node)
        head.next = self.reverseKGroup( node, k)
        return new_head