class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)> len(magazine):
            return False
          
        note_dict= {}
        mag_dict= {}
        for r_char in ransomNote:
            if r_char  not in note_dict:
                note_dict[r_char] = 1
            else:
                note_dict[r_char]+= 1
        for m_char in magazine:
            if m_char not in mag_dict:
                mag_dict[m_char] = 1
            else:
                mag_dict[m_char]+= 1
                
        print(mag_dict)
        print(note_dict)
        for ch in ransomNote:
            print(ch)
            if ch not in mag_dict or mag_dict[ch] < note_dict[ch]:
                return False
        return True
          

       
     
                
     


           
    
            
        
        