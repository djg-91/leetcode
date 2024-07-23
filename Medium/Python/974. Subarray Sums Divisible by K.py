'''
https://leetcode.com/problems/subarray-sums-divisible-by-k

    Given an integer array nums and an integer k, return the number of non-empty 
    subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.

    Example 1:

        Input: nums = [4,5,0,-2,-3,1], k = 5
        Output: 7
        Explanation: There are 7 subarrays with a sum divisible by k = 5:
        [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

    Example 2:

        Input: nums = [5], k = 9
        Output: 0
    
    Constraints:

        1 <= nums.length <= 3 * 104
        -104 <= nums[i] <= 104
        2 <= k <= 104
'''


from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminders = {0 : 1}
        sum = 0
        result = 0
        for num in nums:
            
            sum += num
            reminder = sum % k

            if reminder in reminders:
                result += reminders[reminder]
            else:
                reminders[reminder] = 0

            reminders[reminder] += 1

        return result


if __name__ == '__main__':
    print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))
    print(Solution().subarraysDivByK([5], 9))