class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #we want to work with index.. use enumare to loop
            Sum = sum(nums) # before we loop our right sum is equal to the all the numbers in the array
            right_sum = Sum 
            left_sum = 0 # our left sum is zero 

            for i in range(len(nums)):
                currnum = nums[i] # current number we are at in for loop
                right_sum  = right_sum - currnum
                if left_sum == right_sum:
                    return i
                left_sum +=currnum
            return -1    



            
                
                
          
        