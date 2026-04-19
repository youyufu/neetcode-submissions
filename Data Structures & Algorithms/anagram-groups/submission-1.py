class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash = {}
        for word in strs:
            # make list of char frequency
            chars = [0] * 26
            for char in word:
                chars[ord(char) - 97] += 1
            key = tuple(chars)
            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]
        for key in hash:
            result.append(hash[key])
        return result