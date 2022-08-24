class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
            
        index = len(nums)
      
        for i in range(1,index):
            nums[i] = nums[i] + nums[i-1]
                           
            
        return nums
            
                
            
               
        
     
     
            