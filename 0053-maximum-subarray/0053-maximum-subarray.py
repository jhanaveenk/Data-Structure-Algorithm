class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]
        i=1
        while i < len(nums):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(currSum, maxSum)
            i += 1
        return maxSum