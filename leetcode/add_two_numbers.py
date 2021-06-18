from definitions import ListNode, construct_listnode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_list = ListNode()
        curr_node = sum_list
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_digit = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            next_node = ListNode()
            curr_node.val = sum_digit
            curr_node.next = next_node if (l1 or l2) or carry != 0 else None
            curr_node = next_node
        if carry != 0:
            curr_node.val = carry
        return sum_list
        # Time Complexity: O(N)   Space Complexity: O(1)

if __name__=='__main__':
    sol = Solution()
    assert sol.addTwoNumbers(construct_listnode([2,4,3]), construct_listnode([5,6,4])) == construct_listnode([7,0,8])
    assert sol.addTwoNumbers(construct_listnode([9,9,9,9,9,9,9]), construct_listnode([9,9,9,9])) == construct_listnode([8,9,9,9,0,0,0,1])
    assert sol.addTwoNumbers(construct_listnode([0]), construct_listnode([0])) == construct_listnode([0])
