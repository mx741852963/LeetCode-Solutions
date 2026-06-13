class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        summ = 0
        res = ""
        for word in words:
            summ = 0
            for char in word:
                summ += weights[ord(char) - 97]
            print(summ)
            tem = chr(97 - summ % 26 + 25)
            res += "".join(tem)
        return res 