class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notepad={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in notepad:
                return [notepad[complement],i]
            else:
                notepad[num]=i