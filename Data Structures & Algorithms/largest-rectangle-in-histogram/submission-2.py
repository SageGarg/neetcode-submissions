class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]   # invisible right wall at the end
        stack = []                # indices of bars still waiting for their right wall
        best = 0

        for i, h in enumerate(heights):
            # bar i is shorter, so it's the RIGHT WALL for every taller bar on the stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]          # this bar's turn as the shortest
                left = stack[-1] if stack else -1      # LEFT WALL = next bar down on the stack
                width = i - left - 1                   # right wall - left wall - 1
                best = max(best, height * width)
            stack.append(i)

        return best