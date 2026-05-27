# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = behind = head
        count = 0
        while ahead:
            ahead = ahead.next
            count +=1
        for _ in range(count//2):
            behind=behind.next
        return behind