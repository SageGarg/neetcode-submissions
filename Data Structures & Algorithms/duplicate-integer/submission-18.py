class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for theNum in nums:
            i = nums.index(theNum) + 1
            
            for i in range(len(nums)):
                if theNum == num:
                    return True
            
        return False
        