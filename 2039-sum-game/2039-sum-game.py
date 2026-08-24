class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        def get(nums):
            numbers,qustion_mark = 0,0
            for char in nums:
                if char == '?':
                    qustion_mark+=1
                else :
                    numbers +=int(char)
            return  numbers,qustion_mark 
        l_n ,l_q = get(num[n//2:])
        r_n ,r_q = get(num[:n//2])
        return (l_q+r_q)& 1!= 0 or (r_n+r_q*4.5) !=(l_n+l_q*4.5)
# Time and Space O(n)