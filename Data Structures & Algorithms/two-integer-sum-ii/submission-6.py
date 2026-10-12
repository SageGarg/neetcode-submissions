class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
        myList = []
        # mySet = set(numbers)
        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     # print(complement)
        #     if complement in mySet and numbers.index(complement)>i:
        #         myList.append(i+1)
        #         myList.append(numbers.index(complement)+1)

        l,r = 0,len(numbers) - 1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                myList.append(l+1)
                myList.append(r+1)
                break
        return myList
            
            
            