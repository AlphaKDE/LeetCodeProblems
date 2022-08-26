class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #1. create hashmap to map the values in s to values in t
        
        #2. we need to somhow have both items in an string in a tuple... use ZIP fucntion
        
        #3. use dict to transform the zip into a dictionary or hashmap 
        
        combined_strings = zip(s,t)# this python function combines the two strings into a tuple insite a container
        
     
        
        # hashmap = dict(combined_strings) the dict function change the container making it a dictionary, with each     tuple's first index being a key and the second index being a value.
        # print(hashmap)
        
        occurence_dictt = {}
        occurence_dicts = {}
        for c1,c2 in combined_strings:
            if (c1 not in occurence_dictt) and (c2 not in occurence_dicts):
                occurence_dictt[c1] = c2
                occurence_dicts[c2] = c1
            elif occurence_dictt.get(c1) != c2 or occurence_dicts.get(c2)!= c1:
                return False
        return True 

        
        
        
    
        
#         for key,value in hashmap.items():
#             (c1,c2) = hashmap.items()
#             if key in s and value in t:
#                 return True
#             elif  hashmap.get(value) != key  or hashmap.get(key)!= value:
#                 return False
#         return True
                
     
        
        

    
        