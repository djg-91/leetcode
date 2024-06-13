'''
https://leetcode.com/problems/find-common-characters

    Given a string array words, return an array of all characters that 
    show up in all strings within the words (including duplicates). 
    You may return the answer in any order.

    Example 1:

        Input: words = ["bella","label","roller"]
        Output: ["e","l","l"]

    Example 2:

        Input: words = ["cool","lock","cook"]
        Output: ["c","o"]

    Constraints:

        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of lowercase English letters.
'''


from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        if len(words) == 1: return list(words[0])
        
        res = []

        for i in range(len(words)):
            words[i] = Counter(words[i])

        for k, v in words[0].items():
            valid = True
            for word in words[1:]:
                if k not in word:
                    valid = False
                    break
                else:
                    v = min(word[k], v)

            if valid: 
                res += [k] * v
        
        return res