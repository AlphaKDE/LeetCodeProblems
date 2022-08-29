class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        res = len(nums)
        
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res
        
        
        #1. if we are given [0,n] the amount of numbers in the list will be n+1
#         correct_range = len(nums)
#         correct_sets = set([i for i in range(correct_range+1)]) # creating a hashset to store the correct values given a range 
        
        
                
#         print(correct_sets)
        
        
#         for item in correct_sets:
#             if item not in nums:
#                 return item
#         #time:O(n)
#         #space :O(n)
           
           
        
                
        
            
            
        
        