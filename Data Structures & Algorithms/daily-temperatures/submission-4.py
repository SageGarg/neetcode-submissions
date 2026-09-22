class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)  # pre-fill with 0s
        stack = []  # holds indices of days still waiting for a warmer day

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result