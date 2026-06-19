class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def sp(arr):
            n = len(arr)
            cols = n.bit_length()
            lk =[[0]*cols for _ in range(n)]
            for i in range(n):
                lk[i][0] = arr[i]
            for j in range(1,cols):
                for i in range(0,n-(1<<j)+1):
                    lk[i][j] = math.gcd(lk[i][j-1],lk[i+(1<<j-1)][j-1])
            return lk
        def query(l,r,lk):
            lenn = r - l +1
            j = lenn.bit_length()-1
            return math.gcd(lk[l][j],lk[r-(1<<j)+1][j])
        sp_gcd = sp(nums) 
        n = len(nums)
        total_subarrays = 0
        for i in range(n):
            if nums[i] % k != 0:continue
            left_bound = -1
            low, high = i, n - 1
            while low <= high:
                mid = (low + high) // 2
                current_gcd = query(i, mid, sp_gcd)
                if current_gcd == k:
                    left_bound = mid
                    high = mid - 1
                elif current_gcd > k:low = mid + 1
                else:high = mid - 1
            if left_bound == -1:continue
            right_bound = -1
            low, high = i, n - 1
            while low <= high:
                mid = (low + high) // 2
                current_gcd = query(i, mid, sp_gcd)
                if current_gcd == k:
                    right_bound = mid
                    low = mid + 1
                elif current_gcd > k:low = mid + 1
                else:high = mid - 1
            total_subarrays += (right_bound - left_bound + 1)
        return total_subarrays
