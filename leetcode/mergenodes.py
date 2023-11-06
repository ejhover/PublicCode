class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        try:
            ans = list1 if list1.val <= list2.val else list2
        except:
            ans = list1 if list1 else list2
        while list1 and list2:
            temp1, temp2 = list1.next, list2.next
            p = list1 if list1.val <= list2.val else list2
            p.next = list1 if p==list2 else list2
            try:
                p.next.next = temp1 if temp1.val<temp2.val else temp2
            except:
                p.next.next = temp1 if temp1 else temp2
            list1, list2 = temp1, temp2
        t=ans
        while t:
            print(t.val, end=" ")
            t=t.next
q = Solution()
print(q.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None)))))