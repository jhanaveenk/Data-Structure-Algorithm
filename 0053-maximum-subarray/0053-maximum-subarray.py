class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum=0,nums[0]
        for i in range(len(nums)):
            currSum += nums[i]
            if maxSum < currSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum