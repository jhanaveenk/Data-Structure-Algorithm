class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        n = len(nums)
        for i in nums:
            if nums_dict.get(i) > n //2:
                return i
        else:
            return -1