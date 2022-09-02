class Solution:
    def romanToInt(self, s: str) -> int:
        #s.length is always between 1 and 15 it cannot be greater
        roman = {"I":1, "V": 5, "X": 10, "L": 50, "C":100,
                "D": 500, "M": 1000}
        result = 0 
        print(len(s))
        
        for item in range(len(s)):
            print(item)
            if item + 1 < len(s) and roman[s[item]]< roman[s[item+1]]:
                result -= roman[s[item]]
            else:
                result += roman[s[item]]
                
                
        return result
        
     
            
                

        
