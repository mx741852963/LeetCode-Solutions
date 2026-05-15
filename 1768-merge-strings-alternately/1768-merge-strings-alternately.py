class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_one_len = len(word1)
        word_two_len = len(word2)
        word_flag = 1  # word1
        merged = []
        i = 0
        j = 0
        while i < word_one_len and j < word_two_len:
            if word_flag:
                merged.append(word1[i])
                i += 1
                word_flag = 0
            else:
                merged.append(word2[j])
                j += 1
                word_flag = 1
        if i < word_one_len:
            merged.append(word1[i:])

        if j < word_two_len:
            merged.append(word2[j:])
            
        return "".join(merged)  # Time : O(word1+word2) , Space : O(word1+word2)
