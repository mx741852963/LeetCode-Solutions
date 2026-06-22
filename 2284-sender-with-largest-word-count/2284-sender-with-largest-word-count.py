class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(int)
        for sender, message in zip(senders, messages):
            counter[sender]+=len(message.split())
        max_word = ''
        max_length = 0
        for key,value in counter.items():
            if value > max_length:
                max_length = value
                max_word = key
            elif value == max_length:
                if key > max_word:
                    max_word = key           
        return max_word   
# Time O(n)
# Spcae O(u)