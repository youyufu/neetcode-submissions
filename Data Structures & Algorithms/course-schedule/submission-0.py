class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            premap[a].append(b)
        
        visited = set()

        def dfs(a):
            if a in visited:
                return False
            if premap[a] == []:
                return True
            
            visited.add(a)
            for b in premap[a]:
                if not dfs(b):
                    return False
            visited.remove(a)
            premap[a] = []
            return True
        
        for a in range(numCourses):
            if not dfs(a):
                return False
        return True
