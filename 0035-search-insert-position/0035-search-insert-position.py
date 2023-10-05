class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while r >= l:
            m = l + (r-l)//2
            if nums[m] > target:
                r = m-1
            if nums[m] < target:
                l= m+1
            if nums[m] == target:
                return m
        else:
            return l