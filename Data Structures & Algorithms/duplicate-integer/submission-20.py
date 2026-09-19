class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for theNum in nums:
            i = nums.index(theNum) + 1
            
            for i in range(i,len(nums)):
                if theNum == nums[i]:
                    return True
            
        return False
        