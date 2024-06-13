'''
https://leetcode.com/problems/sort-colors

    Given an array nums with n objects colored red, white, or blue, 
    sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, 
    white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    Example 1:

        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
    
    Example 2:

        Input: nums = [2,0,1]
        Output: [0,1,2]
    
    Constraints:

        n == nums.length
        1 <= n <= 300
        nums[i] is either 0, 1, or 2.
'''


from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)
        pos = 0

        for i in range(3):
            
            if i not in counter: continue
            
            for j in range(counter[i]):
                nums[pos] = i
                pos += 1