class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 1
        num = nums[i]
        for theNum in nums:
            for num in nums:
                if theNum == num:
                    return True
            
        return False
        