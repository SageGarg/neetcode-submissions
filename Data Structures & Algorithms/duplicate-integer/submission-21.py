class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for i in len(nums):
            theNum = nums[i]
            
            for j in range(i+1,len(nums)):
                if theNum == nums[j]:
                    return True
            
        return False
        