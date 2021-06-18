class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        self_start = self
        other_start = other
        while self_start or other_start:
            if not other_start or not self_start:
                return False
            if self_start.val != other_start.val:
                return False
            self_start = self_start.next
            other_start = other_start.next
        return True

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right

def construct_listnode(list):
    '''
    Constructs a ListNode object from a list. Returns the first object in the list.
    '''
    head_node = ListNode(list[0], None)
    prev_node = head_node
    for val in list[1:]:
        curr_node = ListNode(val, None)
        prev_node.next = curr_node
        prev_node = curr_node
    return head_node
