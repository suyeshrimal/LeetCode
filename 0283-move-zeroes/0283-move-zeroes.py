class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        for j in range(len(nums)):
            if nums[j]==0:
                j=j+1
            else:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i=i+1
        return nums

            
        