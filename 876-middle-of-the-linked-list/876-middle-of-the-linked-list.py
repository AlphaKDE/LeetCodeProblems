# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        array = []
        
        count = 0
        
        
        while head is not None:
            array.append(head)
            head = head.next
            count += 1
            
        return array[len(array)//2]
    
    #time complexity = 0(n) # since we are iterating through the linked list
    #space complexity 0(n) # since we are creating a new data structure to store our linked list 
            
        