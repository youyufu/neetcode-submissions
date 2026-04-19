class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for i in range(len(word)):
            if word[i] not in curr_node.children:
                curr_node.children[word[i]] = TrieNode()
            curr_node = curr_node.children[word[i]]
            if i == len(word) - 1:
                curr_node.end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i in range(len(word)):
            if word[i] not in curr_node.children:
                return False
            curr_node = curr_node.children[word[i]]
            if i == len(word) - 1:
                return True if curr_node.end else False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for ch in prefix:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False        