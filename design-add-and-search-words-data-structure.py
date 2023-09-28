class TrieNode:
    def __init__(self):
        self.isend = False
        self.children = [None for _ in range(26)]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for j in word:
            idx = ord(j) - 97
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.isend = True

    def search(self, word: str) -> bool:

        def search_again(index, current):
            if index == len(word):
                return current.isend

            if word[index] == ".":
                for i in range(26):
                    if current.children[i] and search_again(index + 1, current.children[i]):
                        return True
                return False
            else:
                idx = ord(word[index]) - ord('a')
                if not current.children[idx]:
                    return False
                return search_again(index + 1, current.children[idx])

        return search_again(0, self.root)