# leetcode: https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    
    # empty lists return nothing
    if not list1 and not list2:
        return None
    
    res = ListNode()
    
    l1 = list1
    l2 = list2

    # check which list has the lesser val
    while l1 or l2:
        v1 = None
        v2 = None
        
        if l1:
            v1 = l1.val
        if l2:
            v2 = l2.val
        
        if v1 and v2:
            if v1 <= v2:
                res.val = v1
                res.next = ListNode()
                l1 = l1.next
            else:
                res.val = v2
                res.next = ListNode()
                l2 = l2.next       
        elif v1 and not v2:
            res.val = v1
            res.next = ListNode()
            l1 = l1.next
        elif not v1 and v2:
            res.val = v2
            res.next = ListNode()
            l2 = l2.next

    return res