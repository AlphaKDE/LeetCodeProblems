class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0 
        
        
        # loop throught the 2d array
        # add the rows together and return the highest row
       
    
        for costumer  in accounts:
            customerwealth = 0
            for bank in costumer: 
                customerwealth+= bank
                
                
            maxwealth = max(maxwealth,customerwealth)
        
     
    
                
        return maxwealth
                
                
               
               
                
        
       
        
       
     
       
        