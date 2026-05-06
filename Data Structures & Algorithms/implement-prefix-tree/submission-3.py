class TreeNode:
    def __init__(self):
        self.characters = {}
        self.finished = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.characters:
                cur.characters[w] = TreeNode()
            cur = cur.characters[w]
        cur.finished = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.characters:
                return False
            cur = cur.characters[w]
        return cur.finished
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.characters:
                return False
            cur = cur.characters[w]
        return True
    