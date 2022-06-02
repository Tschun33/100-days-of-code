# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        numl = []
        numr = []

        while l1:
            numl.append(l1)
            l1 = l1.next

        num_left = numl[::-1]





sol = Solution()

l1 = ListNode(1, None)



sol.addTwoNumbers()