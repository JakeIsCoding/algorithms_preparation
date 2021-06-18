from typing import List

class Solution:
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dict of value: index pairs.
        nums_hash = {n: i for i,n in enumerate(nums)}
        # Loop over nums, check if complement is in the dict.
        for i, num in enumerate(nums):
            if target - num in nums_hash:
                # Check to make sure element isn't being repeated.
                if i != nums_hash[target - num]:
                    return [i, nums_hash[target-num]]
        return None
        # Time Complexity: O(N), Space Complexity: O(N)

if __name__ == '__main__':
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0,1]
    assert sol.twoSum([3,2,4], 6) == [1,2]
    assert sol.twoSum([3,3], 6) == [0,1]
