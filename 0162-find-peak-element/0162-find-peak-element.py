class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) 
        for i in range(len(nums)):
            if (i == 0 or nums[i] > nums[i-1]) and ( i == n-1 or nums[i] > nums[i+1]):
                return i
        return -1