class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.split(" ")
        # print(x)
        y = "".join(x)
        # print(y)
        cleaned = ''.join(filter(str.isalnum, y))
        lowercase = cleaned.lower()
        print(lowercase)
        for i in range(len(lowercase)):
            if lowercase[i] != lowercase[len(lowercase) - 1 - i]:
                return False
        return True
        