from definitions import ListNode, construct_listnode

class Solution:
    '''
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    next = l1
                    l1 = l1.next
                else:
                    next = l2
                    l2 = l2.next
            elif not l1:
                next = l2
                l2 = l2.next
            else:
                next = l1
                l1 = l1.next
            current.next = next
            current = next
        return head.next
        # Time Complexity: O(N)   Space Complexity: O(1)

if __name__=='__main__':
    sol = Solution()
    assert sol.mergeTwoLists(construct_listnode([]), construct_listnode([])) == construct_listnode([])
    assert sol.mergeTwoLists(construct_listnode([]), construct_listnode([0])) == construct_listnode([0])
    assert sol.mergeTwoLists(construct_listnode([0,3]), construct_listnode([1,4])) == construct_listnode([0,1,3,4])
