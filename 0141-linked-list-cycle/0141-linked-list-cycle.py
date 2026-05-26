# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # sett = set()
        # cur = head 
        # while cur :
        #     if  cur not in sett:
        #         sett.add(cur)
        #         cur = cur.next
        #     else :
        #         return True
        # return False
        # Time O(n)
        # Space O(n)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True 
        return False
        # Time O(n)
        # Space O(1)