class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        hash = defaultdict(list)
        ans = []
        for i in range(len(s)):
            hash[s[i]].append(i)
        for char in hash:
            l = hash[char][0]
            r = hash[char][-1]
            is_valid = True
            i = l
            while i <= r:
                ch = s[i]
                if hash[ch][0] < l:
                    is_valid = False
                    break
                r = max(r, hash[ch][-1])
                i += 1
            if is_valid:
                ans.append([l, r])
        ans.sort(key=lambda x: x[-1])
        result = []
        last_r = -1
        for l, r in ans:
            if l > last_r:
                result.append(s[l : r + 1])
                last_r = r
        return result
    # Space and Time O(n)
