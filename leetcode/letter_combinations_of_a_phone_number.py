from typing import List

class Solution:
    '''
    Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent. Return the answer in
    any order.

    A mapping of digit to letters (just like on the telephone buttons) is given
    below. Note that 1 does not map to any letters.
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {"1": [],
                    "2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        current_strings = [""] if digits else []
        next_strings = []
        for digit in digits:
            new_chars = char_map[digit]
            for string in current_strings:
                for char in new_chars:
                    next_strings.append(string + char)
            current_strings = next_strings
            next_strings = []
        # Time Complexity: Exponential   Space Complexity: Exponential
        return current_strings


if __name__=='__main__':
    sol = Solution()
    assert sol.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
