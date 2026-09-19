class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # //anagram condition: each character same number of times. meaning same length and same frequency of each character
        length_s = len(s)
        length_t = len(t)
        if (length_s != length_t):
            return False
        else:
            sorted_s = "".join(sorted(s))
            sorted_t = "".join(sorted(t))
     
            set_s = set()
            dict_s = {}
            set_t = set()
            dict_t = {}
            i = 0
            j = 0
            for e in sorted_s:
                if e in set_s:
                    dict_s[e] = i
                    i +=1
                
                else:
                    set_s.add(e)
                    dict_s[e] = i
                    i+=1
                    
            
            for e in sorted_t:
                if e in set_t:
                    dict_t[e] = j
                    i+=1
                else:
                    set_t.add(e)
                    dict_t[e] = j
                    j+=1
                


            # now we play with dictionaries
            return dict_s == dict_t
        return False
        