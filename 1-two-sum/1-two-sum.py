
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
#         #O(n^2) time 
#         #0(1) space
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)): # starting at i+1 to not repeat two of the same values.
#                 print(nums[i],nums[j])
#                 if nums[j] == target - nums[i]:
                    
#                     return [i,j]
          #O(n) time O(n) space  
        map = {} # initilizing an empty map 
        
        for index, value in enumerate(nums):
            diff = target - value #
            if diff in map:
                return [map[diff],index]
            map[value] = index
        
        
            
    
    
      
    

            
     
            
        
        
            
            
                
      