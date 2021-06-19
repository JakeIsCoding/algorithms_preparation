from typing import List
class Solution:
    '''
    Given n non-negative integers a1, a2, ..., an , where each represents a point
    at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
    of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
    the x-axis forms a container, such that the container contains the most water.

    Notice that you may not slant the container.
    '''
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = lambda l,r: min([height[l], height[r]]) * (r-l)
        current_max = 0
        while left < right:
            current_area = area(left, right)
            if current_area > current_max:
                current_max = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Time Complexity O(N)   Space Complexity O(1)
        return current_max

if __name__=='__main__':
    sol = Solution()
    assert sol.maxArea([1,1]) == 1
    assert sol.maxArea([4,3,2,1,4]) == 16
    assert sol.maxArea([1,2,1]) == 2
