class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # words to trie
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        res = set()
        visited = set()
        def dfs(i, j, node, wordsofar):
            if (i<0 or j<0 or i>=len(board) or j>=len(board[0])) or ((i,j) in visited) or (board[i][j] not in node.children):
                return
            visited.add((i,j))
            node = node.children[board[i][j]]
            wordsofar = wordsofar + board[i][j]
            if node.end:
                res.add(wordsofar)
            dfs(i-1,j,node,wordsofar)
            dfs(i+1,j,node,wordsofar)
            dfs(i,j-1,node,wordsofar)
            dfs(i,j+1,node,wordsofar)
            visited.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")
        return list(res)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                new = TrieNode()
                curr.children[ch] = new
            curr = curr.children[ch]
        curr.end = True