from typing import List

class Solution:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0
        di, dj = 0,1
        top, right, left, bottom = 0, m, -1, n
        result = []
        while True:
            if j+dj == right and dj == 1:
                di = 1
                dj = 0
                right -=1
                if i + di == bottom: break
            elif i + di == bottom and di == 1:
                di = 0
                dj = -1
                bottom -= 1
                if j + dj == left: break
            elif j + dj == left and dj == -1:
                di = -1
                dj = 0
                left += 1
                if i + di == top: break
            elif i + di == top and di == -1:
                di = 0
                dj = 1
                top += 1
                if j + dj == right: break
            result.append(matrix[i][j])
            i += di
            j += dj
        result.append(matrix[i][j])
        # Time Complexity: O(N* M) Space Complexity: O(N * M)
        return result


if __name__=='__main__':
    sol = Solution()
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
