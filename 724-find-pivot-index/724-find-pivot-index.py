class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #we want to work with index.. use enumare to loop
        S = sum(nums)
        leftsum = 0 
        for index,data in enumerate(nums):
            if leftsum == (S-leftsum - data):
                return index
            leftsum += data
            
        return -1
               
            
                
                
                
            
                
                
          
        