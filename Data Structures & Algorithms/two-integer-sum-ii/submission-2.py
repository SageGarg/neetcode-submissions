class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        myList = []
        mySet = set(numbers)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in mySet and numbers.index(complement)>=i:
                myList.append(i+1)
                myList.append(numbers.index(complement)+1)
        return myList
            
            
            