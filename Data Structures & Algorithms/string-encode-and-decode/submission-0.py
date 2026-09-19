class Solution:

    def encode(self, strs: List[str]) -> str:

        str2 =""
        for word in strs:
            str2+=word+"_"
        print(str2)
     

        return str2


    def decode(self, s: str) -> List[str]:

        result = s.split("_")
        result.pop()
        return result
