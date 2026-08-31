# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # hash = defaultdict(int)
        # hash[1] = head.val
        # enumrate = 2
        # while head:
        #     head = head.next
        #     if head:
        #         hash[enumrate] = head.val
        #         enumrate += 1
        # if len(hash) <= 2:
        #     return [-1, -1]
        # n = len(hash)
        # cp = []

        # for idx in range(2, n):
        #     if hash[idx - 1] > hash[idx] < hash[idx + 1]:
        #         cp.append(idx)
        #     elif hash[idx - 1] < hash[idx] > hash[idx + 1]:
        #         cp.append(idx)
        # if len(cp) < 2:
        #     return [-1,-1]
        # return [ 
        #     min([((cp[x + 1]) - cp[x]) for x in range(len(cp) - 1)]),
        #     cp[-1] - cp[0],
        # ] 
# Time O(n) 
# space O(n)
        min_dist, first, last = float('inf'), -1, -1
        prev, cur, nxt = head, head.next, head.next.next
        i = 1
        while nxt:
            if prev.val > cur.val< nxt.val or prev.val < cur.val> nxt.val:
                if first == -1:
                    first = i
                else :
                    min_dist = min(min_dist, i-last)
                last = i
            i += 1
            prev, cur, nxt = cur, nxt, nxt.next
        if first==last: return [-1,-1]
        return [min_dist, last-first]
# Time O(n) 
# space O(1)