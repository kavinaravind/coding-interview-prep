import pytest
from typing import Optional, List
from datastructures.list_node import ListNode, array_to_list, list_to_array

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return head.next

class TestSolution:
    @pytest.mark.parametrize("list1, list2, expected", [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ])
    def test_merge_two_lists(self, list1: List[int], list2: List[int], expected: List[int]) -> None:
        l1 = array_to_list(list1)
        l2 = array_to_list(list2)
        merged = Solution().merge_two_lists(l1, l2)
        assert list_to_array(merged) == expected