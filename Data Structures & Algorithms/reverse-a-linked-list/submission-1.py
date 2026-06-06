# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        counter = 0
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            counter +=1
        return prev
        
        
        # return [head[i-1] for i in range(len(head), 0, -1)]