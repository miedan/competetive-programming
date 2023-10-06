class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0
   
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True
        current.count += 1

  


    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        current = self.root

        for char in words:
            self.insert(char)

        def index(char, i):

            for j in range(i, len(s)):
                if s[j] == char:
                    return j
            return -1

        def sequence(node, idxo):

            nonlocal ans

            if node.is_end:
                ans += node.count

            for char in node.children:
                idx = index(char, idxo +1)
                if idx != -1:
                    sequence(node.children[char], idx)
            return

        ans = 0
        sequence(current, -1)
        return ans