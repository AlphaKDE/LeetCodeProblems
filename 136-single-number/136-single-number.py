class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        sequence = Counter(nums)
        
        print(sequence)
        
        for count in sequence:
            if sequence[count] == 1:
                return count
            
            
       
            
          
           
        