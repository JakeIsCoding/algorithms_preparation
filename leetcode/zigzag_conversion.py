class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for _ in range(numRows)]
        # Number of chars needed to return to the same row in the zigzag
        len_cycle = 2 * numRows - 2 if numRows > 1 else 1
        for i, c in enumerate(s):
            guess =  i % len_cycle
            # Calculate which row the letter belongs to from its index.
            row = guess if guess < numRows else len_cycle - guess
            result[row].append(c)
        # Time complexity: O(N)   Space Complexity: O(N)
        return "".join(["".join(r) for r in result])




if __name__=='__main__':
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
