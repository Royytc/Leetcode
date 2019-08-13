#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,prev=head,None
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        return prev
        

def stringToListNode(input):
        # Generate list from the input
        numbers = input
    
        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next
    
        ptr = dummyRoot.next
        return ptr
a=Solution()
integerlist=[1,2,3,4,5]
ListNode1=stringToListNode(integerlist)
rev=a.reverseList(ListNode1)
print(rev)
