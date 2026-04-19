class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash = {}
        for word in strs:
            if "".join(sorted(word)) in hash:
                hash["".join(sorted(word))].append(word)
            else:
                hash["".join(sorted(word))] = [word]
        for key in hash:
            result.append(hash[key])
        return result