class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current = 1   # a single number is a streak of 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                current += 1                    # streak continues
            elif nums[i+1] - nums[i] == 0:
                continue                        # duplicate, ignore it
            else:
                longest = max(longest, current) # save before resetting
                current = 1                     # start a new streak

        return max(longest, current)   