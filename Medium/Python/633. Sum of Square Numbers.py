'''
https://leetcode.com/problems/sum-of-square-numbers

    Given a non-negative integer c, decide whether there're 
    two integers a and b such that a2 + b2 = c.

    Example 1:

        Input: c = 5
        Output: true
        Explanation: 1 * 1 + 2 * 2 = 5

    Example 2:

        Input: c = 3
        Output: false
    
    Constraints:

        0 <= c <= 231 - 1
'''


from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        c_sqrt = sqrt(c)

        if c_sqrt.is_integer(): return True
        
        aprox = int(c_sqrt + 1)

        i, j = 0, aprox

        while i <= j:
            sqr = i**2 + j**2
            if sqr == c: 
                return True
            elif sqr > c:
                j -= 1
            elif sqr < c:
                i += 1

        return False 


if __name__ == '__main__':
    print(Solution().judgeSquareSum(1000))