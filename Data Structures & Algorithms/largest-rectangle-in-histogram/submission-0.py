class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # so we need to count how many bars we can go and the height of shortest bar
        # answer could also be height of just one bar

        # we cant' rearrange since order matters.
        stack = []
        largest = max(heights)
        # lets go brute force
        # two direct answers to get max area:  number of bars, height of bar
        # then running two for loops inside it
        best = heights[0]
        for i in range(len(heights)):
            min_h = heights[i]
            for j in range(i,len(heights)):
                min_h = min(min_h, heights[j])
            area = min_h*(j-i+1)
            best = max(best,area)
        return best





        