from definitions import ListNode, construct_listnode

class Solution:
    '''
    Given a linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            new_head = head.next
            current = head
            while current and current.next:
                placeholder = current
                temp = current.next
                current.next = temp.next
                temp.next = current
                current = current.next
                if current and current.next:
                    placeholder.next = current.next
            return new_head
        # Time Complexity O(N)    Space Complexity  O(1)

if __name__=='__main__':
    sol = Solution()
    assert sol.swapPairs(construct_listnode([])) == construct_listnode([])
    assert sol.swapPairs(construct_listnode([1])) == construct_listnode([1])
