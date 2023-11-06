# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
easy way I thought of first. Time = O(N) space = O(N)
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = []
        while True:
            if head == None:
                return False
            if head.next in d:
                return True
            d.append(head)
            head = head.next
'''
Smarter way using tortoise and hare algorithm. Time = O(N) Space = O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while slow != None and fast != None:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
            if slow == fast:
                return True
        return False
            
            