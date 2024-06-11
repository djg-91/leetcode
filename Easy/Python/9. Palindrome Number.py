'''
https://leetcode.com/problems/palindrome-number

    Given an integer x, return true if x is a 
    palindrome, and false otherwise.

    Example 1:

        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
    
    Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
        Therefore it is not a palindrome.
    
    Constraints:

        -231 <= x <= 231 - 1
'''


from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]: return False
            i += 1
            j -= 1

        return True