'''
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''




class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        index = 0
        smallest = len(nums) + 1
        for i,num in enumerate(nums):
            total = total + nums[i]
            while total >= target:
                smallest = min(smallest, i-index+1)
                total = total - nums[index]
                index = index + 1
        return smallest if smallest <= len(nums) else 0