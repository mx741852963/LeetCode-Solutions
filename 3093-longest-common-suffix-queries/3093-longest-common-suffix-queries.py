class TrieNode:
    def __init__(self):
        self.children = {}
        self.smallest = inf
        self.index = inf
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,s,index):
        cur = self.root
        lenn = len(s)
        if lenn < cur.smallest:cur.smallest,cur.index = lenn,index
        for c in s :
            if not c in cur.children : cur.children[c] = TrieNode()
            cur = cur.children[c]
            if lenn < cur.smallest:cur.smallest,cur.index = lenn,index
    def query(self,s):
        cur  = self.root
        for c in s :
            if not c in cur.children : break 
            cur = cur.children[c]
        return cur.index
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie,res = Trie(),[]
        for i ,j in enumerate(wordsContainer):trie.insert(j[::-1],i)
        for i in wordsQuery :res.append(trie.query(i[::-1]))
        return res
# w = len wordsContainer
# lw = avg len word in wordsContainer
# q = len wordsQuery
# qw = avg len word in wordsQuery
# Time O(w*lw+q*qw)
# Space (w*lw)