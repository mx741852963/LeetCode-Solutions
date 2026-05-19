from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        main_text = "balloon"
        hashmap = defaultdict(int)
        counter = 0
        i = 0
        lenn = len(main_text)
        for txt in text:
            hashmap[txt] += 1
        while True:
            if i == lenn :
                i = 0
            char = main_text[i]
            if char == 'n' and hashmap[char] != 0:
                counter += 1
            if hashmap[char] == 0:
                del hashmap[char]
            if char in hashmap:
                hashmap[char] -= 1
                i += 1
            else:
                break
        return counter
