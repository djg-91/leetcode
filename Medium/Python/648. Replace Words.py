'''
https://leetcode.com/problems/replace-words

    In English, we have a concept called root, which can be followed by some other word 
    to form another longer word - let's call this word derivative. 
    For example, when the root "help" is followed by the word "ful", 
    we can form a derivative "helpful".

    Given a dictionary consisting of many roots and a sentence consisting of words 
    separated by spaces, replace all the derivatives in the sentence with the root forming it. 
    If a derivative can be replaced by more than one root, replace it with the root 
    that has the shortest length.

    Return the sentence after the replacement.

    Example 1:

        Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"
    
    Example 2:

        Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
        Output: "a a b c"

    Constraints:

        1 <= dictionary.length <= 1000
        1 <= dictionary[i].length <= 100
        dictionary[i] consists of only lower-case letters.
        1 <= sentence.length <= 106
        sentence consists of only lower-case letters and spaces.
        The number of words in sentence is in the range [1, 1000]
        The length of each word in sentence is in the range [1, 1000]
        Every two consecutive words in sentence will be separated by exactly one space.
        sentence does not have leading or trailing spaces.
'''


from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def change_word(word):
            dummy_dict = dictionary.copy()
            for i in range(len(word)):
                dummy_word = word[0:i]
                dummy_dict = [x for x in dummy_dict if x.startswith(dummy_word)]
                
                if len(dummy_dict) == 0: return word
                
                if dummy_word in dummy_dict: return dummy_word

            return word

        min_len = min([len(x) for x in dictionary])
        words = sentence.split(' ')
        result = []
        for word in words:
            if len(word) < min_len: 
                result.append(word)
                continue

            result.append(change_word(word))

        return ' '.join(result)


if __name__ == '__main__':
    print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))