class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        
        print(hashmap.values())
        for occ in hashmap.values():
            if occ >= 2:
                return True
        return False
            
            
        