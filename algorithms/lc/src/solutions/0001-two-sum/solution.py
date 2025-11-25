import pytest

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in a list that add up to a specific target.

        Approach:
        Uses a hash map to store numbers and their indices in a single pass.
        For each number, it calculates the required complement (`target - num`).
        If the complement is already in the hash map, it returns the indices
        of the complement and the current number. Otherwise, it adds the
        current number and its index to the map.

        Time Complexity: O(n)
            - We iterate through the list of n elements once.
            - Hash map operations (insertion and lookup) are O(1) on average.

        Space Complexity: O(n)
            - In the worst-case scenario, the hash map may store up to n elements.

        Difficulty: Easy
        """
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
    def test_two_sum(self, nums: list[int], target: int, expected: list[int]) -> None:
        assert Solution().two_sum(nums, target) == expected