# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         array = []
        
#         count = 0
        
        
#         while head is not None:
#             array.append(head)
#             head = head.next
#             count += 1
            
#         return array[len(array)//2]
    
    #time complexity = 0(n) # since we are iterating through the linked list
    #space complexity 0(n) # since we are creating a new data structure to store our linked list 
    
        middleNode = head
        endNode = head 

        while endNode != None and endNode.next != None:
            middleNode = middleNode.next
            endNode = endNode.next.next

        return middleNode
    #time complexity O(n) since we are still iterating through the linked list
    #space complexity 0(1) #since no other data structres are being created 

        