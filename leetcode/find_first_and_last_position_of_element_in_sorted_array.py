from typing import List

class Solution:
    """
    Given an array of integers nums sorted in ascending order, find the starting
    and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        min_i = None
        max_i = None
        def binary_search(nums, target, i, j, find_min):
            k = (i + j) // 2
            nonlocal min_i
            nonlocal max_i
            if 0 <= k < len(nums) and nums[k] == target:
                if find_min:
                    min_i = k
                    return binary_search(nums,target, i, k, find_min) if k != j else binary_search(nums,target, i, k-1, find_min)
                else:
                    max_i = k
                    return binary_search(nums,target, k+1, j, find_min)
            elif j-i <=1:
                return -1
            elif nums[k] < target:
                return binary_search(nums, target, k+1, j, find_min)
            else:
                return binary_search(nums, target, i, k, find_min)
        binary_search(nums, target, 0, len(nums), True)
        binary_search(nums, target, 0, len(nums), False)
        if min_i == None and max_i == None:
            return [-1, -1]
        # Time Complexity: O(log N)
        # Space Complexity: O(log N), can be O(1) w/ iterative binary search.
        return [min_i, max_i]


if __name__=='__main__':
    sol = Solution()
    assert sol.searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
    assert sol.searchRange([], 0) == [-1,-1]
