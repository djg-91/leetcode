'''
https://leetcode.com/problems/number-of-good-pairs

    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Example 1:

        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    Example 2:

        Input: nums = [1,1,1,1]
        Output: 6
        Explanation: Each pair in the array are good.

    Example 3:

        Input: nums = [1,2,3]
        Output: 0
    
    Constraints:

        1 <= nums.length <= 100
        1 <= nums[i] <= 100
'''

from typing import List
from collections import Counter
from math import comb 


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {k: v for k, v in Counter(nums).items() if v > 1}
        if len(counter) == 0: return 0

        res = 0
        counter = Counter(counter.values())
        for k, v in counter.items():
            if k == 2:
                res += 1 * v
            else:
                res += comb(k, 2) * v

        return res


if __name__ == '__main__':
    print(Solution().numIdenticalPairs([4,4,2,2]))
    print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
    print(Solution().numIdenticalPairs([1,1,1,1]))
    print(Solution().numIdenticalPairs([1,2,3]))