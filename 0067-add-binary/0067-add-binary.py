class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry
        return bin(a)[2:]


# Time O(a+b)
# Space O(1)
