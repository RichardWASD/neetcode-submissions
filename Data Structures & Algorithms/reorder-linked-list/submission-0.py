# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    U:
        I: head of linked list
        O: Head of the same list, just reordered 
        C: Cant modify the vals themselvs 
        E: Empty list 
    P:
        Split list in half. Then reverse that half of the list then 'Reorder'

        1) go through list once and determine the halfway point : fast pointer
        2) Start at the half point and reverse that sublist
        3) then we will have pointer at front of list, and one at mid point and connect them from there 
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head == None):
            return 
        
        curr = head
        slow = head # mid point 
        fast = head
        prev = None

        while(fast and fast.next): # Gets us postion of mid point
            
            slow= slow.next
            fast = fast.next.next
        

        second = slow.next # Needed to remove infinite loop -> sever the link
        slow.next = None
        prev = None


        while(second): # reverse sub list (adjusted the vars)

            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        while(curr and prev): # start list pointer w/ mid point and link those and increment both 
            temp2 = prev.next
            temp1 = curr.next

            curr.next = prev
            curr = temp1
            prev.next = curr
            prev = temp2


