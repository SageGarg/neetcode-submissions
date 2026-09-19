class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs is array of strings. when you find anagrams put them in sublists
        strs.sort()
        print(strs)
        anagram_arr = []
        for i in range(len(strs)):
            x = strs[i]
            x.sort()
            print(x)
            if i < len(strs) - 1:
                y = strs[i+1]
                y.sort()
                print(y)
                if x == y:
                    anagram_arr.append(x)
                    
        return anagram_arr