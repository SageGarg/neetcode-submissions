class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we know if one number is n then other number is target - n
        # we parse through each number, calc target -n look it up. if exists. then lets find its indices.
        my_set = set(nums)
        for x in nums:
            complement = target - x
            if complement in my_set:
                myList = [nums.index(x),nums.index(complement)]
                return myList


