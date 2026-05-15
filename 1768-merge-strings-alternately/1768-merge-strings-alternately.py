class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for char1, char2 in zip(word1, word2):
            merged.append(char1)
            merged.append(char2)
        min_len = min(len(word1), len(word2))
        return "".join(merged) + word1[min_len:] + word2[min_len:]
            