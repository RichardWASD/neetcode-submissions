# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



'''
U: 
    I: head of 2 different linked list
    O: A linked list where elements from both list are listed in sorted order
    E: Empty list, One list being larger
    C:
I: Make a new linked list and do a check on each list for smaller element and then add to new 
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        dummy = res = ListNode(None)
        curr1 = list1
        curr2 = list2 

        while(curr1 and curr2):
            if(curr1.val <= curr2.val):
                res.next = ListNode(curr1.val)
                curr1 = curr1.next
            elif(curr1.val > curr2.val):
                res.next = ListNode(curr2.val)
                curr2 = curr2.next
            res = res.next
            
           

        if(curr1 and not curr2):
            res.next = curr1
        elif(curr2 and not curr1):
            res.next = curr2
        return dummy.next

        