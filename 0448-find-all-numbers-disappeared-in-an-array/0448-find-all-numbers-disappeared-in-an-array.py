class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_list = set(nums)
        lst = []
        for num in range(1,len(nums)+1):
            if num not in nums_list:
                lst.append(num)
        return lst