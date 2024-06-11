'''
https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 
Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
'''


from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        if words[0] == '': return ''
        prefix = words[0][0]
        i = 1

        while True:
            for word in words:
                char = word[0:i]

                if i > len(word): return char

                if prefix != char:
                    return prefix[:-1] if i > 1 else ''

            i += 1
            prefix = words[0][0:i]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
    print(Solution().longestCommonPrefix(["ab", "a"]))