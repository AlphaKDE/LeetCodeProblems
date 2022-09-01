from array import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #looping through the nums 
        map = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return [map[diff],index]
            map[value] = index
            
    
    
      
    

            
     
            
        
        
            
            
                
      