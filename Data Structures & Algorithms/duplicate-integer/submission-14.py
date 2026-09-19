class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 1
        for num in nums:
            
            if ( i <= len(nums) - 1):

                if (nums[i] == num):
                    return True
                i += 1
        return False
        