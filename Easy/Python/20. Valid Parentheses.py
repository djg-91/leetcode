'''
https://leetcode.com/problems/valid-parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
    
    Example 1:

        Input: s = "()"
        Output: true

    Example 2:

        Input: s = "()[]{}"
        Output: true

    Example 3:

    Input: s = "(]"
    Output: false
    

    Constraints:

        1 <= s.length <= 104
        s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        open_brackets = ['(', '[', '{']
        brackets = [
            ['(', ')'],
            ['[', ']'], 
            ['{', '}']
        ]
        i = 0
        while i < len(s):
            if s[i] in open_brackets: i += 1
            else:
                if i-1 < 0: return False
                if s[i-1:i+1] not in brackets: return False
                s.pop(i)
                s.pop(i-1)
                i -= 1

        return len(s) == 0


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))