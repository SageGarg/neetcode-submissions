class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we know if one number is n then other number is target - n
        # we parse through each number, calc target -n look it up. if exists. then lets find its indices.
        my_dict = {}
        for i in range(len(nums)):
            x = nums[i]
            complement = target - x
            if complement in my_dict:
                return [my_dict[complement], i]
            my_dict[x] = i
                    