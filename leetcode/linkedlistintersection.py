# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 1, 1
        curr = headA
        while curr.next:
            curr = curr.next
            lenA+=1
        curr = headB
        while curr.next:
            curr = curr.next
            lenB+=1
        curr = headA if lenA > lenB else headB
        other = headA if curr == headB else headB
        for i in range(abs(lenB-lenA)):
            curr = curr.next
        while curr:
            if curr == other:
                return curr
            curr = curr.next
            other = other.next
        return
# better solution below
'''
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return q
        
'''