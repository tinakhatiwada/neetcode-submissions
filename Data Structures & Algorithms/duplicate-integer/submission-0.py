class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums=set(nums)
        if len(nums)==len(snums) :
            return False
        else :
            return True

        
   




        