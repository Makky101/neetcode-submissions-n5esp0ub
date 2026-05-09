class Trie:
    def __init__(self):
        self.char = {}
        self.isComplete = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        root = self.root
        for l in word:
            if l not in root.char:
                root.char[l] = Trie()
            root = root.char[l]
        root.isComplete = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            for l in range(j, len(word)):
                char = word[l]
                if char == '.':
                    for char in root.char.values():
                        if dfs(l + 1, char):
                            return True
                    return False
                else:
                    if char not in root.char:
                        return False
                    root = root.char[char]
            return root.isComplete
        
        return dfs(0, self.root)
