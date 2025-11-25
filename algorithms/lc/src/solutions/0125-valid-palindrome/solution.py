import re
import pytest

class Solution:
    def is_palindrome(self, s: str) -> bool:
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