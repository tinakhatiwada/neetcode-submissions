class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=1
            else:
                nums_dict[num]+=1
        sorted_nums_dict=sorted(nums_dict,key=nums_dict.get,reverse=True)
        return(sorted_nums_dict[:k])