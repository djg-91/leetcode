'''
https://leetcode.com/problems/subsets/

    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Example 1:

        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
    Example 2:

        Input: nums = [0]
        Output: [[],[0]]

'''


from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for s in range(1, len(nums) + 1):
            combs = combinations(nums, s)
            result.extend([list(x) for x in combs])

        return result

    
if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))