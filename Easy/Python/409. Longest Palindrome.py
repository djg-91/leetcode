'''
https://leetcode.com/problems/longest-palindrome

    Given a string s which consists of lowercase or uppercase letters, 
    return the length of the longest palindrome
    that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome.

    Example 1:

        Input: s = "abccccdd"
        Output: 7
        Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

    Example 2:

        Input: s = "a"
        Output: 1
        Explanation: The longest palindrome that can be built is "a", whose length is 1.
        
    Constraints:

        1 <= s.length <= 2000
        s consists of lowercase and/or uppercase English letters only.
'''


from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) <= 1: return len(s)
        
        counter = Counter(s)
        res, odd = 0, False

        for k ,v in counter.items():
            if odd is not True and v % 2 == 1:
                odd = True

            res += v // 2

        return (res * 2) + (1 if odd else 0)


if __name__ == '__main__':
    print(Solution().longestPalindrome("abccccdd"))