from typing import List

class Solution:
    """
    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen
    numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times.
     Two combinations are unique if the frequency of at least one of the chosen
     numbers is different.

    It is guaranteed that the number of unique combinations that sum up to target
    is less than 150 combinations for the given input.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursive_helper(candidates, target, current_sols):
            if target < 0:
                return []
            elif target == 0:
                return [current_sols]
            else:
                this_level_sols = []
                for n in candidates:
                    this_level_sols += recursive_helper(candidates, target-n, current_sols + [n])
                return this_level_sols
        solutions = recursive_helper(candidates, target, [])
        unique_solutions = []
        for sol in solutions:
            if sorted(sol) not in unique_solutions:
                unique_solutions.append(sorted(sol))
        return unique_solutions




if __name__=='__main__':
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))
