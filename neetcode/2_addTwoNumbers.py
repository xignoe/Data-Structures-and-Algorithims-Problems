# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2

        arr1 = []
        arr2 = []

        while head1:
            arr1.append(head1.val)
            head1 = head1.next
        
        while head2:
            arr2.append(head2.val)
            head2 = head2.next

        arr1R = []
        arr2R = []

        count1 = len(arr1) - 1
        while (count1 >= 0):
            arr1R.append(arr1[count1])
            count1 -= 1

        count2 = len(arr2) - 1
        while (count2 >= 0):
            arr2R.append(arr2[count2])
            count2 -= 1

        str1 = ''
        str2 = ''
        for i in range(len(arr1R)):
            str1 += str(arr1R[i])

        for j in range(len(arr2R)):
            str2 += str(arr2R[j])

        result = int(str1) + int(str2)

        resStr = str(result)
        helpStr = ''
        count3 = len(resStr) - 1
        while (count3 >= 0):
            helpStr += resStr[count3]
            count3 -= 1


        print(helpStr)

        head = ListNode(int(helpStr[0]))

        current = head

        for char in helpStr[1:]:
            current.next = ListNode(int(char))
            current = current.next
            
        return head