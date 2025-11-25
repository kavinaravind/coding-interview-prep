import pytest
from typing import Optional
from datastructures.list_node import ListNode, array_to_list, list_to_array

class Solution:
    """
    Merges two sorted linked lists into a single sorted linked list.

    Approach:
    Initializes a dummy `head` node to simplify edge cases like an empty result list.
    A `curr` pointer is used to build the new list. It iterates through both lists,
    comparing node values and appending the smaller one to the merged list.
    After one list is exhausted, the remaining part of the other list is appended.
    The merged list starts from `head.next`.

    Time Complexity: O(m + n)
        - We iterate through both lists once, where m and n are their respective lengths.

    Space Complexity: O(1)
        - The new list is created by rearranging the nodes of the original lists,
          not by creating new nodes. Only a constant amount of extra space is used for pointers.

    Difficulty: Easy
    """
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
    def test_merge_two_lists(self, list1: list[int], list2: list[int], expected: list[int]) -> None:
        l1 = array_to_list(list1)
        l2 = array_to_list(list2)
        merged = Solution().merge_two_lists(l1, l2)
        assert list_to_array(merged) == expected