class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def sp(arr,op):
            n = len(arr)
            cols = n.bit_length()
            lk = [[0]*cols for _ in range(n)]
            for i in range(n):lk[i][0] = arr[i]
            for j in range(1,cols):
                for i in range(0,n-(1<<j)+1):
                    lk[i][j] = op(lk[i][j-1],lk[i+(1<<j-1)][j-1])
            return lk
        def query(l,r,lk,op):
            lenn = r - l +1
            j = lenn.bit_length() - 1
            return op(lk[l][j],lk[r-(1<<j)+1][j])
        maxx_sp = sp(nums,max)
        minn_sp = sp(nums,min)
        l = 0
        r = 0
        lenn = len(nums)
        max_sub = 0
        while r <  lenn and l < lenn:
            maxx = query(l,r,maxx_sp,max)
            minn = query(l,r,minn_sp,min)
            tem = abs(maxx -minn)
            while abs(query(l, r, maxx_sp, max) - query(l, r, minn_sp, min)) > limit:
                l += 1
            r+=1
            max_sub = max(max_sub, r - l)
        return max_sub




