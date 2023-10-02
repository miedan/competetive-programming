class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.count = val

    def sum(self, prefix: str) -> int:
        current = self.root

        
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        
        return self.summ(current)

    def summ(self, node: TrieNode) -> int:
      
        ans = node.count
        for child in node.children.values():
            ans += self.summ(child)
        return ans




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)