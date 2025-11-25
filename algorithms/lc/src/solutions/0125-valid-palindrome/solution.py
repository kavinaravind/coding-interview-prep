import re
import pytest

class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

        Approach:
        First, it preprocesses the string by removing all non-alphanumeric characters and converting it to lowercase.
        Then, it uses a two-pointer approach. One pointer starts from the beginning (`l`) and the other from the
        end (`r`). The characters at these pointers are compared. If they don't match at any point, it's not
        a palindrome. The pointers move towards the center until they meet or cross.

        Time Complexity: O(n)
            - The string preprocessing (regex substitution and lowercasing) takes O(n).
            - The two-pointer scan also takes O(n).

        Space Complexity: O(n)
            - A new string is created to store the filtered and lowercased version of the original string.

        Difficulty: Easy
        """
        # 1) convert all uppercase letters into lowercase letters and remove all non-alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # 2) apply two pointers strategy to check if chars match
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("ab_a", True),
    ])
    def test_is_palindrome(self, s: str, expected: bool) -> None:
        assert Solution().is_palindrome(s) is expected