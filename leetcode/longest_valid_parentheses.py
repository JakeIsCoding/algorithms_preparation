from typing import List
from definitions import ListNode, construct_listnode

class Solution:
    '''
    Given a string containing just the characters '(' and ')', find the length
    of the longest valid (well-formed) parentheses substring.
    '''
    def longestValidParentheses(self, s: str) -> int:
        longest_substrings = []
        for i, c in enumerate(s):
            longest_substring = 0
            if c == ")":
                if i > 0 and s[i-1] == "(":
                    longest_substring = longest_substrings[-2] + 2 if len(longest_substrings) > 2 else 2
                elif longest_substrings and i - 1 - longest_substrings[-1] >= 0 and s[i - 1 - longest_substrings[-1]] == "(":
                    longest_substring = longest_substrings[-1] + 2
                    if longest_substring < i:
                        longest_substring += longest_substrings[-longest_substring]
            longest_substrings.append(longest_substring)
        # Time complexity: O(N)   Space Complexity: O(N)
        return max(longest_substrings) if longest_substrings else 0


if __name__=='__main__':
    sol = Solution()
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
