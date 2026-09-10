class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we have to return k most frequent elements in that array nums

        nums.sort(reverse=True)
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
    

        final_list = []
        sorted_nums_dict = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)

        

  
        
        for i in range(k):
            final_list.append(sorted_nums_dict[i][0])
        return final_list

    
    