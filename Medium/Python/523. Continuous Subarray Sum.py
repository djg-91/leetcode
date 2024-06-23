'''
https://leetcode.com/problems/continuous-subarray-sum

    Given an integer array nums and an integer k, return true if nums has a good subarray 
    or false otherwise.

    A good subarray is a subarray where:

        its length is at least two, and
        the sum of the elements of the subarray is a multiple of k.
    
    Note that:

        A subarray is a contiguous part of the array.
        An integer x is a multiple of k if there exists an integer n 
        such that x = n * k. 0 is always a multiple of k.
    
    Example 1:

        Input: nums = [23,2,4,6,7], k = 6
        Output: true
        Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
   
    Example 2:

        Input: nums = [23,2,6,4,7], k = 6
        Output: true
        Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
        42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

    Example 3:

    Input: nums = [23,2,6,4,7], k = 13
    Output: false

    Constraints:

        1 <= nums.length <= 105
        0 <= nums[i] <= 109
        0 <= sum(nums[i]) <= 231 - 1
        1 <= k <= 231 - 1
'''


from typing import List

'''
Fist attempt. Time Limit Exceeded 🫠

    class Solution:
        def checkSubarraySum(self, nums: List[int], k: int) -> bool:
            
            def checkGoodness(num):
                return num % k == 0
            
            for i in range(len(nums)):
                sum = nums[i]
                added = 1
                if checkGoodness(sum) and added > 1: return True

                for j in range(i + 1, len(nums)):
                    sum += nums[j]
                    added += 1
                    if checkGoodness(sum) and added > 1: return True

            return False
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        reminders = {0 : -1}
        
        for i in range(len(nums)):
            
            sum += nums[i]            
            reminder = sum % k

            if reminder not in reminders: 
                reminders[reminder] = i
            elif i - reminders[reminder] > 1: 
                return True
            
        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([0,1,0], 1)) # True
    print(Solution().checkSubarraySum([23,6,9], 6)) # False
    print(Solution().checkSubarraySum([1,2,12], 6)) # False
    print(Solution().checkSubarraySum([0,0], 1)) # True
    print(Solution().checkSubarraySum([2,4,3], 6)) # True
    print(Solution().checkSubarraySum([1,0], 2)) # False
    print(Solution().checkSubarraySum([23,2,4,6,6], 7)) # True
    print(Solution().checkSubarraySum([0], 1)) # False
    print(Solution().checkSubarraySum([23,2,6,4,7], 13))
    print(Solution().checkSubarraySum([5,0,0,0], 3))