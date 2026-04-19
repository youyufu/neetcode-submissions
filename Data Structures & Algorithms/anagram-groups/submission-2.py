class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for string in strs:
            sorted_str = self.count_alph(string)
            if sorted_str in sorted_strs:
                sorted_strs[sorted_str].append(string)
            else:
                sorted_strs[sorted_str] = [string]
        res = []
        for key in sorted_strs:
            res.append(sorted_strs[key])
        return res
    def count_alph(self, string:str) -> tuple:
        count = [0] * 26
        for char in string:
            count[ord(char)-ord('a')] += 1
        return tuple(count)         