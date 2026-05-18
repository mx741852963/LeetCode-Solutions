class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenn = len(numbers)
        i = 0
        j = lenn - 1
        while j != i:
            if numbers[j] + numbers[i] == target:
                return [i+1, j+1]
                break
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            else:
                i += 1
