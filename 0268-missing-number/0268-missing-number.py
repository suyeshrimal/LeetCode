class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num=max(nums)
        for i in range(0,max_num+2):
            if i not in nums:
                return i