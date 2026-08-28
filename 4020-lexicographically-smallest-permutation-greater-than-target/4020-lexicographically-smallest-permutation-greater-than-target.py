class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        prefix = []
        for i in range(n):
            char = target[i]
            if counts[char] > 0:
                prefix.append(char)
                counts[char] -= 1
            else:
                break
        for i in range(len(prefix), -1, -1):
            if i < len(prefix):
                counts[prefix[i]] += 1
                prefix.pop()
            if i >= n:
                continue
            target_char = target[i]
            ss = sorted(counts.keys())
            for char in ss :
                if char > target_char and counts[char] > 0:
                    prefix.append(char)
                    counts[char] -= 1
                    for c in ss:
                        prefix.extend([c] * counts[c])
                    return "".join(prefix)        
        return ""

# Time and Space O(n)
