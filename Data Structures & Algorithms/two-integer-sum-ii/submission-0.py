class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = 0
        another = []
        mySet = set(numbers)
        print(mySet)
        for x in numbers:
            complement = target - x
            if x in another:
                continue
            if target < x:
                break
            if complement in mySet:
                another.append(x)
                another.append(complement)
            
        return another
        