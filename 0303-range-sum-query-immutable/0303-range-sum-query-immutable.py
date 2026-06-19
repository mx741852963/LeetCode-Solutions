class NumArray:

    def __init__(self, nums: List[int]):
        self.nums= nums
        self.lookup = self.buildSparseTableSum(nums)
        self.cols = len(self.lookup[0]) if self.lookup else 0
    def buildSparseTableSum(self,arr):
        n = len(arr)
        cols = n.bit_length()
        lookup = [[0] * cols for _ in range(n)]
        for i in range(n): lookup[i][0] = arr[i]
        for j in range(1, cols):
            for i in range(0, n - (1 << j) + 1):
                lookup[i][j] = lookup[i][j - 1] + lookup[i + (1 << (j - 1))][j - 1]
        return lookup
    def sumRange(self, left: int, right: int) -> int:
        total_sum = 0
        n = self.cols - 1
        for j in range(n, -1, -1):
            if (1 << j) <= (right - left + 1):
                total_sum += self.lookup[left][j]
                left += (1 << j)
                
        return total_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)