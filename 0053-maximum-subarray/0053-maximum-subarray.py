class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum , max_sum = 0, -10001
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = max(max_sum , curr_sum)
            if curr_sum < 0:
                curr_sum = 0
                

        return max_sum