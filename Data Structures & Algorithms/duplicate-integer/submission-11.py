class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            i = 1
            if ( i < len(nums) - 1):

                if (nums[i] == num):
                    return False
                i += 1
        return True
        