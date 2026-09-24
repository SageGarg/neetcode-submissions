class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append()
        return result
        
            

        