class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x *= sign
        digits = []
        result = 0
        max_32_int = 2 ** 31
        # Push digits onto list
        while x != 0:
            digit = x % 10
            x = x // 10
            digits.append(digit)
        # Loop through digits in reverse order
        for i, digit in enumerate(digits[::-1]):
            if (max_32_int - 1) - result  < digit * 10 ** i:
                # Case where result = - 2^31 should still work.
                if not (sign == -1 and max_32_int - result == digit * 10 ** i):
                    return 0
            result += digit * 10 ** i
        # Time Complexity: O(N) (digits)   Space complexity: O(N)
        # (provided digits[::-1] has a reasonable implementation)
        return sign * result

if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(0) == 0
