class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        new_set = set([item for item in range(1,len(nums)+1)])
        result_array = new_set - set(nums)
        
        return list(result_array)
        
     
        