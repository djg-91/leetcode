'''
https://leetcode.com/problems/search-insert-position

    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, 
    return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

        Input: nums = [1,3,5,6], target = 5
        Output: 2

    Example 2:

        Input: nums = [1,3,5,6], target = 2
        Output: 1

    Example 3:

        Input: nums = [1,3,5,6], target = 7
        Output: 4
    
    Constraints:

        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums contains distinct values sorted in ascending order.
        -104 <= target <= 104
'''


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(target - 1, -2, -1):
            if i >= len(nums): continue
            if nums[i] == target: 
                return i
            elif nums[i] < target:
                return i + 1
            
        return 0


if __name__ == '__main__':
    print(Solution().searchInsert([-1,3,5,6], 0))
    print(Solution().searchInsert([3,6,7,8,10], 5))
    print(Solution().searchInsert([1,3,5,6], 0))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 7))