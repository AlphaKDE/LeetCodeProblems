class Solution:
    def isPalindrome(self, x: int) -> bool:
        String = str(x)
        
        Reversed = String[::-1]
        
        print(String)
        
        print(Reversed)
        
        if String == Reversed:
            return True 
        return False
        