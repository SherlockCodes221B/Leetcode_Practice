'''
Move Zeroes

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        init_pos = 0
        for x in nums:
            if x != 0:
                nums[init_pos] = x
                init_pos += 1
        while init_pos < len(nums):
            nums[init_pos] = 0
            init_pos += 1