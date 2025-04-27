# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #dummy sits at the start of the linkedlist (the head)
        #temp is going to move forward to find which value to add to the list
        dummy = temp = ListNode(0)
        #While both lists contain values, traverse through the sorted lists
        #Resolves edge case where no values are in sorted lists
        while l1 != None and l2 != None:
            #When the value of list 1 is greater than list 2
            #Add value to new linked list and move to the next value in that list
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            #When the value of list 2 is greater than list 1
            #Add value to new linked list and move to the next value in that list
            else:
                temp.next = l2
                l2 = l2.next
            #Move to the next value in the new linked list
            temp = temp.next
        #Attach whichever list is not empty to the new linked list
        #At the end of merging attach the leftover nodes in both lists
        #For example, if list 1 is empty then attaches the rest of l2
        temp.next = l1 or l2
        return dummy.next