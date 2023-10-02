class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
   
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

    def max_len(self, word:str) -> int:
        
        count = 0
        current = self.root
        current.is_end = True
        
        for w in word:
            
            
            # current = current.children[w]
                
            if current.is_end:
                
                current = current.children[w]
                count += 1
            else:
                print("oo")
                return 0

        return count
        




    def longestWord(self, words: List[str]) -> str:
        
        ans = ""
        count = 0
        l = 0

        for word in words:
            self.insert(word)
        for word in words:
            l = self.max_len(word)

            if l > count:
                count = l
                ans = word

            if l == count and word < ans:
                ans = word

        return ans