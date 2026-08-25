class Trie:
    def __init__(self):
        self.children = {}
        self.end_folder = False
    
    def add(self,path):
        curr = self
        for f in path.split("/"):
            if f not in curr.children:
                curr.children[f] = Trie()
            curr = curr.children[f]
        curr.end_folder = True
    
    def prefix(self,path):
        curr = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            curr = curr.children[folders[i]]
            if curr.end_folder:
                return True
        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)
        
        res = []
        for f in folder:
            if not trie.prefix(f):
                res.append(f)
        return res