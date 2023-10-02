class TrieNode:
    def __init__(self):
        self.is_end = False
        self.count = 0
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
            current.count += 1   
            
        current.is_end = True
        

    def score(self, word:str) -> int:

        current = self.root
        count = 0
        for char in word:

            current = current.children[char] 
            count += current.count
        return count

           

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = [0] * len(words)
        for i in words:
            self.insert(i)

        
        for i in range(len(words)):
            word = words[i]
            # print(self.score(word))
            ans[i] += self.score(word)

        return ans