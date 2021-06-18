class Solution:
    '''
    Given a string s, find the length of the longest substring without repeating characters.
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        left = 0
        right = 0
        added_chars = set([])
        max_length = 0
        while right < len(s):
            if s[right] not in added_chars:
                added_chars.add(s[right])
                right += 1
                # Only need to check when expanding the substring.
                if len(added_chars) > max_length:
                    max_length=len(added_chars)
            else:
                added_chars.remove(s[left])
                left += 1
        # Time Complexity: O(N)   Space Complexity: O(N)
        return max_length


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
