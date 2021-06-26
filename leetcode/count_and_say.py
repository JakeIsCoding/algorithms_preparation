from typing import List

class Solution:
    """
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
    which is then converted into a different digit string.

    To determine how you "say" a digit string, split it into the minimal number of
    groups so that each group is a contiguous section all of the same character. Then
    for each group, say the number of characters, then say the character. To convert
    the saying into a digit string, replace the counts with a number and concatenate
    every saying.

    Given a positive integer n, return the nth term of the count-and-say sequence.
    """

    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            digit_string = self.countAndSay(n-1)
            answer_string = []
            prev_c = digit_string[0]
            count = 1
            for c in digit_string[1:]:
                if c == prev_c:
                    count += 1
                else:
                    answer_string.append(str(count) + prev_c)
                    count = 1
                    prev_c = c
            answer_string.append(str(count) + prev_c)
            # Time Complexity: O(?)      # Space Complexity: O(N)
            # Time complexity is difficult; it is N * len(digit_string), the
            # second of which has a very nontrivial dependence on N.
            # Space complexity is O(N): N recursive calls, N for mutating
            # digit string, and N for answer string, so 3*N = N.
            return "".join(answer_string)


if __name__=='__main__':
    sol = Solution()
    assert sol.countAndSay(1) == "1"
    assert sol.countAndSay(4) == "1211"
