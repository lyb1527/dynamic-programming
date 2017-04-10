'''
GIven a sequence of integers, find the longest increasing subsequence, LIS
Return the length of the LIS

What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given
sequence in which the subsequence's elements are in sorted order, lowest to highest,
and in which the subsequence is as long as possible. This subsequence is
 not necessarily contiguous, or unique.

For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
'''

class Solution:

    #@param nums: The integer array
    #@return: The length of LIS (longest increasing subsequence)

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in xrange(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)
