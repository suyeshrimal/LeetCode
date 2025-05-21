class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        nums_dict = {}
        for i,num in enumerate(sorted_nums):
            if num not in nums_dict:
                nums_dict[num]=i
        res = [nums_dict[num] for num in nums]
        return res