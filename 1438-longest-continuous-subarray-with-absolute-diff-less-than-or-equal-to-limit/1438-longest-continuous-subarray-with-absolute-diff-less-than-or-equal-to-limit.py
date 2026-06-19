class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        if n == 0: return 0
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1
        cols = n.bit_length()
        st_max = [[0] * cols for _ in range(n)]
        st_min = [[0] * cols for _ in range(n)]
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
        for j in range(1, cols):
            for i in range(0, n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
        l = 0
        max_sub = 0
        for r in range(n):
            j = lg[r - l + 1]
            curr_max = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            curr_min = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            while curr_max - curr_min > limit:
                l += 1
                j = lg[r - l + 1]
                curr_max = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
                curr_min = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            max_sub = max(max_sub, r - l + 1)  
        return max_sub
        # def sp(arr,op):
        #     n = len(arr)
        #     cols = n.bit_length()
        #     lk = [[0]*cols for _ in range(n)]
        #     for i in range(n):lk[i][0] = arr[i]
        #     for j in range(1,cols):
        #         for i in range(0,n-(1<<j)+1):
        #             lk[i][j] = op(lk[i][j-1],lk[i+(1<<j-1)][j-1])
        #     return lk
        # def query(l,r,lk,op):
        #     lenn = r - l +1
        #     j = lenn.bit_length() - 1
        #     return op(lk[l][j],lk[r-(1<<j)+1][j])
        # maxx_sp = sp(nums,max)
        # minn_sp = sp(nums,min)
        # l = 0
        # r = 0
        # lenn = len(nums)
        # max_sub = 0
        # while r <  lenn and l < lenn:
        #     maxx = query(l,r,maxx_sp,max)
        #     minn = query(l,r,minn_sp,min)
        #     tem = abs(maxx -minn)
        #     while abs(query(l, r, maxx_sp, max) - query(l, r, minn_sp, min)) > limit:
        #         l += 1
        #     r+=1
        #     max_sub = max(max_sub, r - l)
        # return max_sub




