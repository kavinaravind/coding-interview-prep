import pytest
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

class TestSolution:
    @pytest.mark.parametrize("nums, target, expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ])
    def test_two_sum(self, nums: List[int], target: int, expected: List[int]) -> None:
        assert Solution().two_sum(nums, target) == expected