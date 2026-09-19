class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in range (len (nums)):
            product *= nums[i]
        print (product)
        result = []
        for i in range (len(nums)):
            the_num = nums[i]
            if the_num != 0:
                element = int(product / the_num)
            else:
                element 
            result.append(element)
        
        return result

            