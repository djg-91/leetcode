'''
https://leetcode.com/problems/sum-of-all-subset-xor-totals

    The XOR total of an array is defined as the bitwise XOR of all its elements, 
    or 0 if the array is empty.

    For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
    Given an array nums, return the sum of all XOR totals for every subset of nums. 

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by 
    deleting some (possibly zero) elements of b.

    Example 1:

        Input: nums = [1,3]
        Output: 6
        Explanation: The 4 subsets of [1,3] are:
        - The empty subset has an XOR total of 0.
        - [1] has an XOR total of 1.
        - [3] has an XOR total of 3.
        - [1,3] has an XOR total of 1 XOR 3 = 2.
        0 + 1 + 3 + 2 = 6
'''

from typing import List
from itertools import combinations
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0
        subsets = []

        for s in range(1, len(nums) + 1):
            subset = combinations(nums, s)
            subsets.extend(subset)

        for subset in [list(x) for x in subsets]:
            total += subset[0] if len(subset) == 1 else reduce(lambda x, y: x ^ y, subset)
        
        return total


if __name__ == '__main__':
    print(Solution().subsetXORSum([1,3]))
    print(Solution().subsetXORSum([5,1,6]))