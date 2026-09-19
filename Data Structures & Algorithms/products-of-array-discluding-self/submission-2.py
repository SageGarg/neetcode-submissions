class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)):
            product =1
            for j in range(len(nums)):
                x = nums[i]
                nums[i] = 1
                
                product*=nums[j]
                nums[i] = x
            result.append(product)
        return result