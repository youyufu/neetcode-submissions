class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for i in range(len(word)):
            if word[i] not in curr_node.children:
                curr_node.children[word[i]] = TrieNode()
            curr_node = curr_node.children[word[i]]
            if i == len(word) - 1:
                curr_node.end = True

    def search(self, word: str) -> bool:
        def dfs(d, root):
            curr = root

            for i in range(d, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]
            return curr.end
        
        return dfs(0, self.root)

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False