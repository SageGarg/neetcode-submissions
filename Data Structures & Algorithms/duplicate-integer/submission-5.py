class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            i = 1
            if (nums[i] == num):
                return false
            # i += 1
            else:
                return true
        