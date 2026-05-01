class TreeNode:
    def __init__(self):
        self.character = {}
        self.completed = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.character:
                cur.character[c] = TreeNode()
            cur = cur.character[c]
        cur.completed = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.character:
                return False
            cur = cur.character[c] 
        return cur.completed

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.character:
                return False
            cur = cur.character[c]
        return True
        