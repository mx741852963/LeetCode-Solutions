class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # lenn = len(temperatures)
        # for tem in range(lenn):
        #     l = temperatures[tem]
        #     for i in range(tem,lenn):
        #         r = temperatures[i]
        #         if l < r :
        #             temperatures[tem] = i - tem
        #             break
        #         else:
        #             temperatures[tem] = 0
        # return temperatures
        lenn = len(temperatures)
        tem = temperatures
        ans= [0]*lenn
        stk = []
        for i,t in enumerate(tem):
            while stk and stk[-1][0] < t:
                stk_t,stk_i = stk.pop()
                ans[stk_i] = i - stk_i
            stk.append((t,i))
        return ans