class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
            
        
        
        
        
        
        
        
        
        
        
        
        hashmap = Counter(nums) # we set up a counter that counts the occ of the values in nums 
        
        print(hashmap.values()) # testing to see if it outputs the correct values 
        for occ in hashmap.values(): # looping over the values
            if occ >= 2:
                return True
        return False
            
#         #time complexity: O(n) - where n is the numbers in the array
#         #space complexity: O(n) - we are creating a new data structure to store the occurances of the n
            
        
        
        
        