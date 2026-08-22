class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p = 1
        s = 0
        nums = n 
        while n :
            tem = n % 10 
            n //= 10 
            s +=tem
            p *= tem 
        return (nums%(p+s)) == 0