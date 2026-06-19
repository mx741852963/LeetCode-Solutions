class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Time O(n log n ) 
        # Spcae O(n log n )
        # def buildSparseTableMax(arr):
        #     n = len(arr)
        #     lookup = [[0] * (int(math.log(n, 2)) + 1) for _ in range(n + 1)]
        #     for i in range(n):
        #         lookup[i][0] = arr[i]
        #     for j in range(1, int(math.log(n, 2)) + 1):
        #         for i in range(0, n - (1 << j) + 1):
        #             if lookup[i][j - 1] > lookup[i + (1 << (j - 1))][j - 1]:
        #                 lookup[i][j] = lookup[i][j - 1]
        #             else:
        #                 lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
        #     return lookup

        # # Time O(n log n ) 
        # # Spcae O(n log n )
        # def buildSparseTableMin(arr):
        #     n = len(arr)
        #     lookup = [[0] * (int(math.log(n, 2)) + 1) for _ in range(n + 1)]
        #     for i in range(n):
        #         lookup[i][0] = arr[i]
        #     for j in range(1, int(math.log(n, 2)) + 1):
        #         for i in range(0, n - (1 << j) + 1):
        #             if lookup[i][j - 1] < lookup[i + (1 << (j - 1))][j - 1]:
        #                 lookup[i][j] = lookup[i][j - 1]
        #             else:
        #                 lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
        #     return lookup

        # # Time O(1)
        # def query_min(L, R, lookup):
        #     j = int(math.log(R - L + 1, 2))
        #     if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:
        #         return lookup[L][j]
        #     else:
        #         return lookup[R - (1 << j) + 1][j]

        # # Time O(1)
        # def query_max(L, R, lookup):
        #     j = int(math.log(R - L + 1, 2))
        #     if lookup[L][j] >= lookup[R - (1 << j) + 1][j]:
        #         return lookup[L][j]
        #     else:
        #         return lookup[R - (1 << j) + 1][j]
        def buildSparseTable(arr, op):
            n = len(arr)
            cols = n.bit_length()
            lookup = [[0] * cols for _ in range(n)]
            for i in range(n): lookup[i][0] = arr[i]
            for j in range(1, cols):
                for i in range(0, n - (1 << j) + 1):
                    lookup[i][j] = op(lookup[i][j - 1], lookup[i + (1 << (j - 1))][j - 1])
            return lookup
        def query(L, R, lookup, op):
            length = R - L + 1
            j = length.bit_length() - 1
            return op(lookup[L][j], lookup[R - (1 << j) + 1][j])


        lookup_max = buildSparseTable(nums,max)
        lookup_min = buildSparseTable(nums,min)
        lenn = len(nums)
        r = lenn - 1
        count = 0
        heap = []
        # Time O(n log n ) 
        # Spcae O(log n )
        for i in range(lenn):
            maxx = query(i, lenn - 1, lookup_max,max)
            minn = query(i, lenn - 1, lookup_min,min)
            j = maxx - minn
            heapq.heappush(heap, (-j, i, r))
        m = 0
        # Time O(k log n)
        while k:
            num, m, r = heapq.heappop(heap)
            count += num
            if r-1 >= m:
                r = r - 1
                maxx = query(m, r, lookup_max,max)
                minn = query(m, r, lookup_min,min)
                j = maxx - minn
                heapq.heappush(heap, (-j, m, r))
            k -= 1
        return -count
# Time O((n+k) log n)
# Spcae O(n log n )