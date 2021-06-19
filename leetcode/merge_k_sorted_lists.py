from typing import List
from definitions import ListNode, construct_listnode
import heapq

class Solution:
    '''
    You are given an array of k linked-lists lists, each linked-list is sorted
    in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        current = head
        # Construct initial priority queue
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        while heap:
            _, i_min, min_node = heapq.heappop(heap)
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i_min, min_node.next))
            current.next = min_node
            current = min_node
            lists[i_min] = lists[i_min].next
        # Time complexity: O(Nk logk)    Space Complexity:  O(k)
        # Nk total elements, log k to push to heap.
        return head.next




if __name__=='__main__':
    sol = Solution()
    assert sol.mergeKLists([construct_listnode(x) for x in [[1,4,5],[1,3,4],[2,6]]]) == construct_listnode([1,1,2,3,4,4,5,6])
