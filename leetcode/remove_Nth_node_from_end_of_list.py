from typing import List
from definitions import ListNode, construct_listnode

class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the
    list and return its head.
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(float('inf'), head)
        current = head
        N_runner = current
        while current.next:
            if N_runner == current:
                for _ in range(n):
                    N_runner = N_runner.next
            if not N_runner:
                break
            else:
                prev = prev.next
                current = current.next
                N_runner = N_runner.next
        prev.next = current.next
        return head if head != current else prev.next




if __name__=='__main__':
    sol = Solution()
    assert sol.removeNthFromEnd(construct_listnode([1,2,3,4,5]), 2) == construct_listnode([1,2,3,5])
    assert sol.removeNthFromEnd(construct_listnode([1]), 1) == construct_listnode([])
    assert sol.removeNthFromEnd(construct_listnode([1,2]), 1) == construct_listnode([1])
