'''
https://leetcode.com/problems/longest-substring-without-repeating-characters

    Given a string s, find the length of the longest 
    substring without repeating characters.

    Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
    Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        
        def isValid(w):
            return len(set(w)) == len(w)

        k, curr = 0, 0
        
        for i in range(len(s)):
            while i + k < len(s):
                curr += 1
                w = s[i:i + curr]
                if not isValid(w): 
                    curr = k
                    break
                k = curr

        return k
    

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("uqinntq"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))