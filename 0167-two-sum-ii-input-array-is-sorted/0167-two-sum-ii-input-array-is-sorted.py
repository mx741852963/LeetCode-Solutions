class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenn = len(numbers)
        i = 0
        j = lenn - 1
        while True:
            summ = numbers[j] + numbers[i]
            if summ == target:
                return [i+1, j+1]
                break
            if summ > target:
                j -= 1
            else:
                i += 1
# Time O(n)
# Space O(1)