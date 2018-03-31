# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1_cur = l1
        l2_cur = l2
        
        sum = l1.val + l2.val
        memorized = int(sum > 9)
        sum = sum % 10
        
        ans = ListNode(sum)
        ans_cur = ans
        
        while l1_cur.next or l2_cur.next:
            sum = memorized
            
            if l1_cur.next:
                l1_cur = l1_cur.next
                sum += l1_cur.val
            
            if l2_cur.next:
                l2_cur = l2_cur.next
                sum += l2_cur.val
            
            memorized = int(sum > 9)
            sum = sum % 10
            
            ans_cur.next = ListNode(sum)
            ans_cur = ans_cur.next
        
        if memorized:
            ans_cur.next = ListNode(1)
        
        return ans


def list_node_to_num(l: ListNode) -> int:
    multiplier = 10
    sum = l.val
    tmp = l
    
    while tmp.next:
        tmp = tmp.next
        sum += tmp.val * multiplier
        multiplier *= 10
    
    return sum
    

solver = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Explanation: 342 + 465 = 807.
assert 807 == list_node_to_num(solver.addTwoNumbers(l1, l2))