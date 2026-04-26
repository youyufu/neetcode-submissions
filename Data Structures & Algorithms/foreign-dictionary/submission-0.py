class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # graph with chars as nodes
        graph = {}
        for word in words:
            for char in word:
                graph[char] = set()
        
        # fill edges
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited: # cycle
                return visited[char]
            
            visited[char] = True

            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for char in graph:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)
