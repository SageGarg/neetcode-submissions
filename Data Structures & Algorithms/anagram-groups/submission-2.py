class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs is array of strings. when you find anagrams put them in sublists
        strs.sort()
        anagram_arr = []
        for i in range(len(strs)):
            x = strs[i]
            if i < len(strs) - 1:
                y = strs[i+1]
                if x == y:
                    anagram_arr.append(x)
        return anagram_arr

        
        