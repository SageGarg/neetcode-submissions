class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]



        return list(anagram_dict.values())        


        # lets first find if two strings are anagrams
        # strs.sort()
        # x = strs[0]
        # y = strs[1]
        # anagram_str1 = []
        # x2 = "".join(sorted(x))
        # y2 = "".join(sorted(y))

        # if x2 == y2:
        #     anagram_str1.append(x)
        #     anagram_str1.append(y)
        

        # # strs is array of strings. when you find anagrams put them in sublists
        # strs.sort()
        # print(strs)
        # anagram_arr = []
        # for i in range(len(strs)):
        #     x = strs[i]
        #     x2 = "".join(sorted(x))
        #     print(x)
        #     if i < len(strs) - 1:
        #         y = strs[i+1]
        #         y2 = "".join(sorted(y))
        #         print(y)
        #         if x2 == y2:
        #             anagram_arr.append(x)    
        # return anagram_arr