class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Converting integer to string
        s = str(x)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        # Time Complexity: O(N) Space Complexity: O(N)
        # N is the number of digits, O(log(N)) in terms of the magntide.
        return True

    def isPalindrome_int(self, x:int) -> bool:
        # No string conversion
        digits = []
        if x < 0:
            return False
        while x != 0:
            digits.append(x % 10)
            x //= 10
        left = 0
        right = len(digits) - 1
        while left < right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__=='__main__':
    sol = Solution()
    assert sol.isPalindrome(121) == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(10) == False
