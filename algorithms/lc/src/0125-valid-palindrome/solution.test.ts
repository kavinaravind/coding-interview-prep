import { isPalindrome } from './solution';

describe('Is Palindrome', () => {
  test('should return true for "A man, a plan, a canal: Panama"', () => {
    const s = 'A man, a plan, a canal: Panama';
    expect(isPalindrome(s)).toBe(true);
  });

  test('should return false for "race a car"', () => {
    const s = 'race a car';
    expect(isPalindrome(s)).toBe(false);
  });

  test('should return true for an empty or whitespace string', () => {
    const s = ' ';
    expect(isPalindrome(s)).toBe(true);
  });
});
