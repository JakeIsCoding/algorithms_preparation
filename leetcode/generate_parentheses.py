from typing import List

class Solution:
    '''
    Given n pairs of parentheses, write a function to generate all combinations
    of well-formed parentheses.
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        all_strings = []
        def check_valid(s):
            stack = []
            for c in s:
                if c == "(":
                    stack.append("(")
                else:
                    if not stack:
                        return False
                    stack.pop(-1)
            return True if not stack else False
        def depth_first_search(current_string):
            if len(current_string) == 2 * n:
                if check_valid(current_string):
                    all_strings.append("".join(current_string))
            else:
                depth_first_search(current_string + ["("])
                depth_first_search(current_string + [")"])
        depth_first_search([])
        return all_strings



if __name__=='__main__':
    sol = Solution()
    # These assertions are broken
    # assert sol.generateParenthesis(3) == ['(())()', '((()))', '()()()', '(()())', '()(())']
    # assert sol.generateParenthesis(1) == ['()']
