from typing import List

class Solution:
    '''
    Given a string s, return the longest palindromic substring in s.
    '''
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = [0, 1]
        # Treat every character in the string as a potential center.
        for right, c in enumerate(s):
            left = right
            # Loop over central characters until at the edge.
            while left > 0 and s[left]==c:
                left -= 1
            right += 1
            # Iterate until unequal characters are found
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > max_palindrome[1] - max_palindrome[0]:
                max_palindrome = [left+1, right]
        # Time Complexity O(N^2)   Space Complexity O(N)
        # String slicing is O(N) space in python, in a different language this may be O(1).
        return s[max_palindrome[0]:max_palindrome[1]]


if __name__=='__main__':
    sol = Solution()
    assert sol.longestPalindrome("babad") == "bab" or sol.longestPalindrome("babad") == "aba"
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") == "a" or sol.longestPalindrome("ac") == "c"
