class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid =[char.lower() for char in s if char.isalnum()]
        return valid == valid[::-1]
    #     valid =[char.lower() for char in s if char.isalnum()]
    #     lenn= len(valid) // 2
    #     for i in range(lenn):
    #         if valid[i] != valid[-i - 1]:
    #             return False
    #     return True
    # # Time = O(n)
    # # Space = O(n)
