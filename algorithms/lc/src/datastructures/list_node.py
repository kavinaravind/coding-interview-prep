from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def array_to_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def list_to_array(head: Optional[ListNode]) -> List[int]:
    arr: List[int] = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr
