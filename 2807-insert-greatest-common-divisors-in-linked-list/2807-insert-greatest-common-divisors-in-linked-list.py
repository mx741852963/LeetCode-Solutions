# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head 
        cur = head.next
        while cur :
            gcd = math.gcd(cur.val,prev.val) # m
            g = ListNode(gcd)
            prev.next , g.next = g , cur 
            prev , cur = cur ,cur.next
        return head
# Time O(n*m)
# Space O(n)