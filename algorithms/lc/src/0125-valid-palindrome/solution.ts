export function isPalindrome(s: string): boolean {
  // 1) convert all uppercase letters into lowercase letters and remove all non-alphanumeric characters
  s = s.toLowerCase().replace(/[^a-zA-Z]/g, '');

  // 2) apply two pointers strategy to check if chars match
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) {
      return false;
    }
    l++;
    r--;
  }

  return true;
}
